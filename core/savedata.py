# -*- coding: utf-8 -*-
import logging

import core.os_utils
import core.logger

import sqlalchemy
import sqlalchemy.orm

from core.models import EmModelBase, EmApiKey, EmKeyValue


class SaveData:

    current_db_revision = 3

    def __init__(self):
        self._logger = core.logger.get_logger(__name__, logging.DEBUG)
        self.user_settings_file = core.os_utils.get_savedata_directory() + '/settings.db'
        self._logger.debug('SaveData: using savedata file: {}'.format(self.user_settings_file))
        self._logger.info('SaveData: SQLAlchemy version: {}'.format(sqlalchemy.__version__))
        #
        # SQL Alchemy objects
        self.sql_engine = sqlalchemy.create_engine('sqlite:///'+self.user_settings_file, echo=False)
        EmModelBase.metadata.create_all(self.sql_engine)
        # sqlalchemy session
        session_class = sqlalchemy.orm.sessionmaker(bind=self.sql_engine)
        self.sql_session = session_class()
        # check database version for a possible upgrade
        self._check_database()

    def _check_database(self):
        # get db version
        dbrev = self._get_db_revision()
        self._logger.debug('Got savedata db revision: {}'.format(dbrev))
        if dbrev == 0:
            self._run_migration(0)
        else:
            # run migration scripts in order [1..current]
            while dbrev < self.current_db_revision:
                self._run_migration(dbrev)
                dbrev += 1
        self._logger.debug('Savedata DB check complete')

    def _get_db_revision(self) -> int:
        res = self.sql_session.query(EmKeyValue).filter_by(key='_db_version').one_or_none()
        if res is None:
            return 0
        rev = int(res.value)
        return rev

    def _set_db_revision(self, rev: int):
        keyvalue = self.sql_session.query(EmKeyValue).filter_by(key='_db_version').one_or_none()
        if keyvalue is None:
            keyvalue = EmKeyValue('_db_version', str(rev))
        keyvalue.value = str(rev)
        self.sql_session.add(keyvalue)
        self.sql_session.commit()

    def _run_migration(self, rev: int):
        if rev == 0:
            self._logger.debug('First run; set savedata db revision to current = {}'.format(self.current_db_revision))
            self._set_db_revision(self.current_db_revision)
        elif rev == 1:
            self._logger.debug('Running migration rev 1->2...')
            with self.sql_engine.connect() as con:
                con.execute('ALTER TABLE emapikey ADD COLUMN friendly_name TEXT')
                self._set_db_revision(rev+1)
        elif rev == 2:
            self._logger.debug('Running migration rev 2->3...')
            with self.sql_engine.connect() as con:
                con.execute('ALTER TABLE emapikey ADD COLUMN key_type TEXT')
                con.execute('ALTER TABLE emapikey ADD COLUMN access_mask INTEGER')
                con.execute('ALTER TABLE emapikey ADD COLUMN expire_ts INTEGER')
                self._set_db_revision(rev+1)

    def get_apikeys(self) -> list:
        ret = self.sql_session.query(EmApiKey).all()
        return ret

    def get_apikey_by_keyid(self, keyid: str) -> EmApiKey:
        ret = self.sql_session.query(EmApiKey).filter_by(keyid=keyid).one_or_none()
        return ret

    def store_apikey(self, apikey: EmApiKey, check_existing: bool=True):
        res = self.sql_session.query(EmApiKey).filter_by(keyid=apikey.keyid).one_or_none()
        can_add = True
        if check_existing and (res is not None):
            can_add = False  # already exists
        if not can_add:
            self._logger.error('SaveData: cannot add new apikey, already exists: {}'.format(apikey))
            return False
        if res is None:
            self.sql_session.add(apikey)  # add new
        else:
            apikey.id = res.id  # make sure primary keys match before merging
            self.sql_session.merge(apikey)  # update existing
        self.sql_session.commit()
        self._logger.debug('SaveData: Stored apikey: {}'.format(apikey))
        return True

    def remove_apikey_by_keyid(self, keyid: str):
        self.sql_session.query(EmApiKey).filter_by(keyid=keyid).delete()
        self.sql_session.commit()
