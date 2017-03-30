# -*- coding: utf-8 -*-
import logging

import core.os_utils
import core.logger


class EVEData:
    def __init__(self):
        self._logger = core.logger.get_logger(__name__, logging.DEBUG)
        self.datadir = core.os_utils.get_program_directory() + '/evedata'
        #
        self._logger.debug('EVEData: using eve data dir: {}'.format(self.datadir))
