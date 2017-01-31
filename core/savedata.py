# -*- coding: utf-8 -*-
import logging
import sqlite3

import core.os_utils
import core.logger


class SaveData:
    def __init__(self):
        self.logger = core.logger.get_logger(__name__, logging.DEBUG)
        self.user_settings_file = core.os_utils.get_savedata_directory() + '/settings.db'
        self.logger.debug('SaveData: using savedata file: {}'.format(self.user_settings_file))
        pass
