# -*- coding: utf-8 -*-
import logging

import core.logger
import core.os_utils

import evelink.cache.sqlite


class EmCache(evelink.cache.sqlite.SqliteCache):
    def __init__(self):
        self._logger = core.logger.get_logger(__name__, logging.DEBUG)
        path = core.os_utils.get_savedata_directory() + '/cache.db'
        self._logger.debug('EmCache: using cache SQLite db file: {}'.format(path))
        super(EmCache, self).__init__(path)
