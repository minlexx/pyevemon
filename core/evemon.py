# -*- coding: utf-8 -*-
import logging

import core.logger
import core.evedata
import core.savedata


_g_evemoncore_instance = None


class EVEMonCore:
    def __init__(self):
        self.logger = core.logger.get_logger(__name__, logging.DEBUG)
        self.savedata = core.savedata.SaveData()
        self.evedata = core.evedata.EVEData()


def get_evemon_instance() -> EVEMonCore:
    global _g_evemoncore_instance
    if _g_evemoncore_instance is None:
        _g_evemoncore_instance = EVEMonCore()
    return _g_evemoncore_instance
