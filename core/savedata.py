# -*- coding: utf-8 -*-
import logging

import core.os_utils
import core.logger

import sqlalchemy
import sqlalchemy.orm

import core.models


class SaveData:
    def __init__(self):
        self._logger = core.logger.get_logger(__name__, logging.DEBUG)
        self.user_settings_file = core.os_utils.get_savedata_directory() + '/settings.db'
        self._logger.debug('SaveData: using savedata file: {}'.format(self.user_settings_file))
        self._logger.info('SaveData: SQLAlchemy version: {}'.format(sqlalchemy.__version__))
        #
        # SQL Alchemy objects
        self.sql_engine = sqlalchemy.create_engine('sqlite:///'+self.user_settings_file, echo=True)
        core.models.EmModelBase.metadata.create_all(self.sql_engine)
        # sqlalchemy session
        session_class = sqlalchemy.orm.sessionmaker(bind=self.sql_engine)
        self.sql_session = session_class()

    def get_apikeys(self) -> list:
        ret = self.sql_session.query(core.models.EMApiKey).all()
        return ret

    def store_apikey(self, apikey: core.models.EMApiKey):
        res = self.sql_session.query(core.models.EMApiKey).\
            filter_by(keyid=apikey.keyid).one_or_none()
        if res is None:
            self.sql_session.add(apikey)
            self.sql_session.commit()
            self._logger.debug('SaveData: Stored apikey: {}'.format(apikey))
            return True
        self._logger.error('SaveData: cannot add new apikey, already exists: {}'.format(apikey))
        return False
