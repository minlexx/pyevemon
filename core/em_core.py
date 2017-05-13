# -*- coding: utf-8 -*-
import core.logger
import core.evedata
import core.savedata
import core.em_cache
import core.models
import version

import evelink
import evelink.api
import evelink.account
import evelink.constants
import evelink.char
import evelink.eve
import evelink.server

_g_emcore_instance = None


class EmCore:

    # Api key types
    KEY_TYPE_ACCOUNT = evelink.constants.ACCOUNT
    KEY_TYPE_CHARACTER = evelink.constants.CHARACTER
    KEY_TYPE_CORPORATION = evelink.constants.CORPORATION

    def __init__(self):
        self._logger = core.logger.get_logger(__name__)
        self.savedata = core.savedata.SaveData()
        self.evedata = core.evedata.EVEData()
        self.cache = core.em_cache.EmCache()
        # create evelink API object
        ver = version.get_pyevemon_version()
        # "pyevemon/0.1 (alexey.min@gmail.com)"
        self.user_agent_str = '{}/{} ({}) evelink/{}'.format(
            ver['app_name'], ver['version'], ver['author_email'], evelink.__version__)
        self.api = evelink.api.API(cache=self.cache, user_agent=self.user_agent_str)
        self.apicalls_dict = {}
        self._last_error_code = 0
        self._last_error_msg = ''
        #
        self._init_supported_apicalls()

    def _append_apicall_handler(self, apicall_name: str):
        handler_name = 'apicall_' + apicall_name.replace('/', '_')
        handler_func = getattr(self, handler_name, None)
        if handler_func is not None:
            self.apicalls_dict[apicall_name] = handler_func
        else:
            self._logger.error('No handler exists for call "{}"'.format(apicall_name))

    def _init_supported_apicalls(self):
        # explicitly add all supported eveapi calls:
        self._append_apicall_handler('server/ServerStatus')
        self._append_apicall_handler('account/APIKeyInfo')
        self._append_apicall_handler('account/AccountStatus')
        self._append_apicall_handler('account/Characters')
        self._append_apicall_handler('eve/CharacterInfo')
        self._append_apicall_handler('char/CharacterSheet')
        self._append_apicall_handler('char/Skills')
        self._append_apicall_handler('char/SkillQueue')

    def get_supported_apicalls(self) -> list:
        ret = []
        for apicall_name in self.apicalls_dict.keys():
            ret.append(apicall_name)
        return ret

    def set_apikey(self, apikey: core.models.EmApiKey):
        # should be a tuple of (keyid, vcode)
        self.api.api_key = (apikey.keyid, apikey.vcode)

    def _clear_last_error(self):
        self._last_error_code = 0
        self._last_error_msg = ''

    def get_last_error(self) -> tuple:
        return (self._last_error_code, self._last_error_msg)

    # can return list or dict
    def api_call(self, apicall_path: str, **kwargs):
        self._logger.debug('api_call({}) with kwargs={}'.format(apicall_path, kwargs))
        self._clear_last_error()

        try:
            handler_func = self.apicalls_dict[apicall_path]
        except KeyError:
            self._logger.error('No handler to call "{}"'.format(apicall_path))
            self._last_error_code = -1
            self._last_error_msg = 'No handler to call {}'.format(apicall_path)
            return None

        try:
            if len(kwargs.keys()) == 0:
                result_dict = handler_func()
            else:
                result_dict = handler_func(**kwargs)
            # self._logger.debug('Returning: {}'.format(result_dict))
            return result_dict
        except evelink.api.APIError as apiex:
            self._logger.error('API Error {}: {}'.format(apiex.code, apiex.message))
            self._last_error_code = apiex.code
            self._last_error_msg = apiex.message
            return None

    # ============================================================
    # API Calls, that are proxied to evelink
    # ============================================================
    # Client application generally should not use the following
    # methods directly, but use EmCore.api_call('...') wrapper
    # instead, because it catches evelink exceptions.
    # Or, alternatively, you can catch them yourself.
    # ============================================================

    def apicall_server_ServerStatus(self) -> dict:
        srv = evelink.server.Server(api=self.api)
        api_result = srv.server_status()
        return api_result.result

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

    def apicall_eve_CharacterInfo(self, char_id: int) -> dict:
        eve = evelink.eve.EVE(self.api)
        api_result = eve.character_info_from_id(char_id)
        return api_result.result

    def apicall_char_CharacterSheet(self, char_id: int) -> dict:
        char = evelink.char.Char(char_id, self.api)
        api_result = char.character_sheet()
        return api_result.result

    def apicall_char_Skills(self, char_id: int) -> dict:
        char = evelink.char.Char(char_id, self.api)
        api_result = char.skills()
        return api_result.result

    def apicall_char_SkillQueue(self, char_id: int) -> dict:
        char = evelink.char.Char(char_id, self.api)
        api_result = char.skill_queue()
        return api_result.result


def get_core_instance() -> EmCore:
    global _g_emcore_instance
    if _g_emcore_instance is None:
        _g_emcore_instance = EmCore()
    return _g_emcore_instance
