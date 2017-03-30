# -*- coding: utf-8 -*-
import logging

import core.logger
import core.evedata
import core.savedata
import core.em_cache
import core.models
import version

import evelink.api

_g_emcore_instance = None


class EmCore:
    def __init__(self):
        self._logger = core.logger.get_logger(__name__, logging.DEBUG)
        self.savedata = core.savedata.SaveData()
        self.evedata = core.evedata.EVEData()
        self.cache = core.em_cache.EmCache()
        # create evelink API object
        ver = version.get_pyevemon_version()
        # "pyevemon/0.1 (alexey.min@gmail.com)"
        self.user_agent_str = '{}/{} ({})'.format(
            ver['app_name'], ver['version'], ver['author_email'])
        self.api = evelink.api.API(cache=self.cache, user_agent=self.user_agent_str)

    def set_apikey(self, apikey: core.models.EMApiKey):
        # should be a tuple of (keyid, vcode)
        self.api.api_key = (apikey.keyid, apikey.vcode)


def get_core_instance() -> EmCore:
    global _g_emcore_instance
    if _g_emcore_instance is None:
        _g_emcore_instance = EmCore()
    return _g_emcore_instance
