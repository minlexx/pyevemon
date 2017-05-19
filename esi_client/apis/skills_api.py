# coding: utf-8

"""
    EVE Swagger Interface

    An OpenAPI for EVE Online

    OpenAPI spec version: 0.4.6
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class SkillsApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def get_characters_character_id_skillqueue(self, character_id, **kwargs):
        """
        Get character's skill queue
        List the configured skill queue for the given character  ---  This route is cached for up to 120 seconds
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_characters_character_id_skillqueue(character_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int character_id: Character id of the target character (required)
        :param str datasource: The server name you would like data from
        :param str token: Access token to use, if preferred over a header
        :param str user_agent: Client identifier, takes precedence over headers
        :param str x_user_agent: Client identifier, takes precedence over User-Agent
        :return: list[GetCharactersCharacterIdSkillqueue200Ok]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_characters_character_id_skillqueue_with_http_info(character_id, **kwargs)
        else:
            (data) = self.get_characters_character_id_skillqueue_with_http_info(character_id, **kwargs)
            return data

    def get_characters_character_id_skillqueue_with_http_info(self, character_id, **kwargs):
        """
        Get character's skill queue
        List the configured skill queue for the given character  ---  This route is cached for up to 120 seconds
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_characters_character_id_skillqueue_with_http_info(character_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int character_id: Character id of the target character (required)
        :param str datasource: The server name you would like data from
        :param str token: Access token to use, if preferred over a header
        :param str user_agent: Client identifier, takes precedence over headers
        :param str x_user_agent: Client identifier, takes precedence over User-Agent
        :return: list[GetCharactersCharacterIdSkillqueue200Ok]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['character_id', 'datasource', 'token', 'user_agent', 'x_user_agent']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_characters_character_id_skillqueue" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'character_id' is set
        if ('character_id' not in params) or (params['character_id'] is None):
            raise ValueError("Missing the required parameter `character_id` when calling `get_characters_character_id_skillqueue`")


        collection_formats = {}

        resource_path = '/v2/characters/{character_id}/skillqueue/'.replace('{format}', 'json')
        path_params = {}
        if 'character_id' in params:
            path_params['character_id'] = params['character_id']

        query_params = {}
        if 'datasource' in params:
            query_params['datasource'] = params['datasource']
        if 'token' in params:
            query_params['token'] = params['token']
        if 'user_agent' in params:
            query_params['user_agent'] = params['user_agent']

        header_params = {}
        if 'x_user_agent' in params:
            header_params['X-User-Agent'] = params['x_user_agent']

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = ['evesso']

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='list[GetCharactersCharacterIdSkillqueue200Ok]',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_characters_character_id_skills(self, character_id, **kwargs):
        """
        Get character skills
        List all trained skills for the given character  ---  This route is cached for up to 120 seconds
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_characters_character_id_skills(character_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int character_id: An EVE character ID (required)
        :param str datasource: The server name you would like data from
        :param str token: Access token to use, if preferred over a header
        :param str user_agent: Client identifier, takes precedence over headers
        :param str x_user_agent: Client identifier, takes precedence over User-Agent
        :return: GetCharactersCharacterIdSkillsOk
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_characters_character_id_skills_with_http_info(character_id, **kwargs)
        else:
            (data) = self.get_characters_character_id_skills_with_http_info(character_id, **kwargs)
            return data

    def get_characters_character_id_skills_with_http_info(self, character_id, **kwargs):
        """
        Get character skills
        List all trained skills for the given character  ---  This route is cached for up to 120 seconds
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_characters_character_id_skills_with_http_info(character_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int character_id: An EVE character ID (required)
        :param str datasource: The server name you would like data from
        :param str token: Access token to use, if preferred over a header
        :param str user_agent: Client identifier, takes precedence over headers
        :param str x_user_agent: Client identifier, takes precedence over User-Agent
        :return: GetCharactersCharacterIdSkillsOk
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['character_id', 'datasource', 'token', 'user_agent', 'x_user_agent']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_characters_character_id_skills" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'character_id' is set
        if ('character_id' not in params) or (params['character_id'] is None):
            raise ValueError("Missing the required parameter `character_id` when calling `get_characters_character_id_skills`")


        collection_formats = {}

        resource_path = '/v3/characters/{character_id}/skills/'.replace('{format}', 'json')
        path_params = {}
        if 'character_id' in params:
            path_params['character_id'] = params['character_id']

        query_params = {}
        if 'datasource' in params:
            query_params['datasource'] = params['datasource']
        if 'token' in params:
            query_params['token'] = params['token']
        if 'user_agent' in params:
            query_params['user_agent'] = params['user_agent']

        header_params = {}
        if 'x_user_agent' in params:
            header_params['X-User-Agent'] = params['x_user_agent']

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = ['evesso']

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='GetCharactersCharacterIdSkillsOk',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
