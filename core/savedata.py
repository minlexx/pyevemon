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
        print(ret)
        return ret
