# -*- coding: utf-8 -*-
import logging

import core.logger
import core.evedata
import core.savedata
import core.em_cache


_g_emcore_instance = None


class EmCore:
    def __init__(self):
        self._logger = core.logger.get_logger(__name__, logging.DEBUG)
        self.savedata = core.savedata.SaveData()
        self.evedata = core.evedata.EVEData()
        self.cache = core.em_cache.EmCache()


def get_core_instance() -> EmCore:
    global _g_emcore_instance
    if _g_emcore_instance is None:
        _g_emcore_instance = EmCore()
    return _g_emcore_instance
