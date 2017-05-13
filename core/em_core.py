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


def get_evelink_version_str() ->str:
    """
    This function was created specifically not to expose evelink internals
    to client code.
    :return: evelink version string, for example '0.7.5'
    """
    return evelink.__version__


class EmCore:
    """
    This class was created as a wrapper around evelink library and container for all
    objects and classes needed to correctly fetch information from EVE Online API keys.
    It manages EVE XML API requests, stores results in cache until expiration to avoid
    unnecessary network activity and handles network errors.
    
    Also it stores all user settings and data (added api keys, setting etc) using
    SaveData class (self.savedata). This is considered public and can be used by
    client code.
    
    Also it has access to sqlite database containing EVE database dump by
    fullworks.co.uk using EVEData class (self.evedata). This is also considered public
    and can be used directly by client code.
    
    Client code should not create objects of this class directly, but use singleton
    through get_core_instance().
    
    Ideally, client code should only use, rely on core.em_core and core.models
    (well, maybe also core.logger), not using other internals directly (it is
    possible, though).
    """

    # Api key types
    KEY_TYPE_ACCOUNT = evelink.constants.ACCOUNT
    KEY_TYPE_CHARACTER = evelink.constants.CHARACTER
    KEY_TYPE_CORPORATION = evelink.constants.CORPORATION

    def __init__(self):
        self._logger = core.logger.get_logger(__name__)
        self._cache = core.em_cache.EmCache()
        # public
        self.savedata = core.savedata.SaveData()
        self.evedata = core.evedata.EVEData()
        # create evelink API object
        ver = version.get_pyevemon_version()
        # 'pyevemon/0.1 (alexey.min@gmail.com) evelink/0.7.5'
        self._user_agent_str = '{}/{} ({}) evelink/{}'.format(
            ver['app_name'], ver['version'], ver['author_email'], evelink.__version__)
        self._api = evelink.api.API(cache=self._cache, user_agent=self._user_agent_str)
        self._apicalls_dict = {}
        self._last_error_code = 0
        self._last_error_msg = ''
        #
        self._init_supported_apicalls()

    def _append_apicall_handler(self, apicall_name: str):
        handler_name = 'apicall_' + apicall_name.replace('/', '_')
        handler_func = getattr(self, handler_name, None)
        if handler_func is not None:
            self._apicalls_dict[apicall_name] = handler_func
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
        """
        Return a list of strings, supported apicalls.
        :return: List[str]
        """
        ret = []
        for apicall_name in self._apicalls_dict.keys():
            ret.append(apicall_name)
        return ret

    def set_apikey(self, apikey: core.models.EmApiKey):
        """
        Client code should use this method to change API key details
        before sending API request, if needed.
        :param apikey: should be a tuple of (keyid, vcode)
        :return: None
        """
        self._api.api_key = (apikey.keyid, apikey.vcode)

    def _clear_last_error(self):
        self._last_error_code = 0
        self._last_error_msg = ''

    def get_last_error(self) -> tuple:
        """
        Client code uses this to get last error details.
        Result wraps evelink.api.APIError in case of evelink error;
        otherwise error_code might be -1.
        :return: tuple of (error_code, error_message)
        """
        return (self._last_error_code, self._last_error_msg)

    def api_call(self, apicall_path: str, **kwargs):
        """
        Client code uses this method to send network requests (EVE API calls).
        
        If request is in cache, and cache not expired, quickly returns result from cache,
        not sending network request.
        
        Will return None and try to set last error information (see get_last_error())
        in the case of errors.
        
        :param apicall_path: str, name of apicall, for example 'char/CharacterSheet'
        :param kwargs: parameters for call, for char/ apicalls for example: char_id=1234567
        :return: parsed result, as dict (or tuple/list). Depends on api call
        """
        self._logger.debug('api_call({}) with kwargs={}'.format(apicall_path, kwargs))
        self._clear_last_error()

        try:
            handler_func = self._apicalls_dict[apicall_path]
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
        srv = evelink.server.Server(api=self._api)
        api_result = srv.server_status()
        return api_result.result

    def apicall_account_APIKeyInfo(self) -> dict:
        acc = evelink.account.Account(api=self._api)
        api_result = acc.key_info()
        return api_result.result

    def apicall_account_AccountStatus(self) -> dict:
        acc = evelink.account.Account(api=self._api)
        api_result = acc.status()
        return api_result.result

    def apicall_account_Characters(self) -> dict:
        acc = evelink.account.Account(api=self._api)
        api_result = acc.characters()
        return api_result.result

    def apicall_eve_CharacterInfo(self, char_id: int) -> dict:
        eve = evelink.eve.EVE(self._api)
        api_result = eve.character_info_from_id(char_id)
        return api_result.result

    def apicall_char_CharacterSheet(self, char_id: int) -> dict:
        char = evelink.char.Char(char_id, self._api)
        api_result = char.character_sheet()
        return api_result.result

    def apicall_char_Skills(self, char_id: int) -> dict:
        char = evelink.char.Char(char_id, self._api)
        api_result = char.skills()
        return api_result.result

    def apicall_char_SkillQueue(self, char_id: int) -> dict:
        char = evelink.char.Char(char_id, self._api)
        api_result = char.skill_queue()
        return api_result.result


def get_core_instance() -> EmCore:
    """
    Client code should use this to access one single application-global
    instance of EmCore object.
    :return: EmCore single instance
    """
    global _g_emcore_instance
    if _g_emcore_instance is None:
        _g_emcore_instance = EmCore()
    return _g_emcore_instance
