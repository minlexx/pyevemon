# -*- coding: utf-8 -*-
import logging

import core.os_utils
import core.logger

import sqlalchemy
import sqlalchemy.orm

from core.models import EmModelBase, EmApiKey, EmKeyValue


class SaveData:

    current_db_revision = 1

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
        self._logger.debug('Got db revision: {}'.format(dbrev))
        if dbrev < self.current_db_revision:
            # run migration scripts?
            while dbrev < self.current_db_revision:
                self._run_migration(dbrev)
                dbrev += 1
        self._logger.debug('DB check complete')

    def _get_db_revision(self) -> int:
        res = self.sql_session.query(EmKeyValue).filter_by(key='_db_version').one_or_none()
        if res is None:
            return 0
        rev = int(res.value)
        return rev

    def _run_migration(self, rev: int):
        if rev == 0:
            self._logger.debug('Running migration rev 0->1...')
            with self.sql_engine.connect() as con:
                con.execute('ALTER TABLE emapikey ADD COLUMN friendly_name TEXT')
                con.execute("""INSERT OR REPLACE INTO emkeyvalue (key, value)
                    VALUES ('_db_version', '1')""")

    def get_apikeys(self) -> list:
        ret = self.sql_session.query(EmApiKey).all()
        return ret

    def store_apikey(self, apikey: EmApiKey):
        res = self.sql_session.query(EmApiKey).filter_by(keyid=apikey.keyid).one_or_none()
        if res is None:
            self.sql_session.add(apikey)
            self.sql_session.commit()
            self._logger.debug('SaveData: Stored apikey: {}'.format(apikey))
            return True
        self._logger.error('SaveData: cannot add new apikey, already exists: {}'.format(apikey))
        return False
