# -*- coding: utf-8 -*-
import logging

import core.logger
import core.evedata
import core.savedata


_g_emcore_instance = None


class EmCore:
    def __init__(self):
        self.logger = core.logger.get_logger(__name__, logging.DEBUG)
        self.savedata = core.savedata.SaveData()
        self.evedata = core.evedata.EVEData()


def get_core_instance() -> EmCore:
    global _g_emcore_instance
    if _g_emcore_instance is None:
        _g_emcore_instance = EmCore()
    return _g_emcore_instance
