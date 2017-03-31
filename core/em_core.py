# -*- coding: utf-8 -*-
import logging

import core.logger
import core.evedata
import core.savedata
import core.em_cache
import core.models
import version

import evelink.api
import evelink.account

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
        self.apicalls_dict = {}
        self._init_supported_apicalls()

    def _append_apicall_handler(self, apicall_name: str):
        handler_name = 'apicall_' + apicall_name.replace('/', '_')
        handler_func = getattr(self, handler_name, None)
        if handler_func is not None:
            self.apicalls_dict[apicall_name] = handler_func
        else:
            self._logger.error('No handler exists for call "{}"'.format(apicall_name))

    def _init_supported_apicalls(self):
        self._append_apicall_handler('account/APIKeyInfo')
        self._append_apicall_handler('account/AccountStatus')
        self._append_apicall_handler('account/Characters')

    def get_supported_apicalls(self) -> list:
        ret = []
        for apicall_name in self.apicalls_dict.keys():
            ret.append(apicall_name)
        return ret

    def set_apikey(self, apikey: core.models.EMApiKey):
        # should be a tuple of (keyid, vcode)
        self.api.api_key = (apikey.keyid, apikey.vcode)

    def api_call(self, apicall_path: str) -> dict:
        try:
            handler_func = self.apicalls_dict[apicall_path]
            result_dict = handler_func()
            return result_dict
        except evelink.api.APIError as apiex:
            self._logger.error('API Error {}: {}'.format(apiex.code, apiex.message))
            return None
        except KeyError:
            self._logger.error('No handler to call "{}"'.format(apicall_path))
            return None

    def apicall_account_APIKeyInfo(self) -> dict:
        acc = evelink.account.Account(api=self.api)
        api_result = acc.key_info()
        return api_result.result

    def apicall_account_AccountStatus(self) -> dict:
        acc = evelink.account.Account(api=self.api)
        api_result = acc.status()
        return api_result.result

    def apicall_account_Characters(self) -> dict:
        acc = evelink.account.Account(api=self.api)
        api_result = acc.characters()
        return api_result.result


def get_core_instance() -> EmCore:
    global _g_emcore_instance
    if _g_emcore_instance is None:
        _g_emcore_instance = EmCore()
    return _g_emcore_instance
