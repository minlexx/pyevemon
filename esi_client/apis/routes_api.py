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


class RoutesApi(object):
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

    def get_route_origin_destination(self, destination, origin, **kwargs):
        """
        Get route
        Get the systems between origin and destination  ---  This route is cached for up to 86400 seconds
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_route_origin_destination(destination, origin, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int destination: destination solar system ID (required)
        :param int origin: origin solar system ID (required)
        :param list[int] avoid: avoid solar system ID(s)
        :param list[list[int]] connections: connected solar system pairs
        :param str datasource: The server name you would like data from
        :param str flag: route security preference
        :param str user_agent: Client identifier, takes precedence over headers
        :param str x_user_agent: Client identifier, takes precedence over User-Agent
        :return: list[int]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_route_origin_destination_with_http_info(destination, origin, **kwargs)
        else:
            (data) = self.get_route_origin_destination_with_http_info(destination, origin, **kwargs)
            return data

    def get_route_origin_destination_with_http_info(self, destination, origin, **kwargs):
        """
        Get route
        Get the systems between origin and destination  ---  This route is cached for up to 86400 seconds
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_route_origin_destination_with_http_info(destination, origin, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int destination: destination solar system ID (required)
        :param int origin: origin solar system ID (required)
        :param list[int] avoid: avoid solar system ID(s)
        :param list[list[int]] connections: connected solar system pairs
        :param str datasource: The server name you would like data from
        :param str flag: route security preference
        :param str user_agent: Client identifier, takes precedence over headers
        :param str x_user_agent: Client identifier, takes precedence over User-Agent
        :return: list[int]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['destination', 'origin', 'avoid', 'connections', 'datasource', 'flag', 'user_agent', 'x_user_agent']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_route_origin_destination" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'destination' is set
        if ('destination' not in params) or (params['destination'] is None):
            raise ValueError("Missing the required parameter `destination` when calling `get_route_origin_destination`")
        # verify the required parameter 'origin' is set
        if ('origin' not in params) or (params['origin'] is None):
            raise ValueError("Missing the required parameter `origin` when calling `get_route_origin_destination`")

        if 'avoid' in params and len(params['avoid']) > 100:
            raise ValueError("Invalid value for parameter `avoid` when calling `get_route_origin_destination`, number of items must be less than or equal to `100`")
        if 'connections' in params and len(params['connections']) > 100:
            raise ValueError("Invalid value for parameter `connections` when calling `get_route_origin_destination`, number of items must be less than or equal to `100`")

        collection_formats = {}

        resource_path = '/v1/route/{origin}/{destination}/'.replace('{format}', 'json')
        path_params = {}
        if 'destination' in params:
            path_params['destination'] = params['destination']
        if 'origin' in params:
            path_params['origin'] = params['origin']

        query_params = {}
        if 'avoid' in params:
            query_params['avoid'] = params['avoid']
            collection_formats['avoid'] = 'csv'
        if 'connections' in params:
            query_params['connections'] = params['connections']
            collection_formats['connections'] = 'csv'
        if 'datasource' in params:
            query_params['datasource'] = params['datasource']
        if 'flag' in params:
            query_params['flag'] = params['flag']
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
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='list[int]',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
