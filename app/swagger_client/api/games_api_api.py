# coding: utf-8

"""
    ICFP Contest 2020 API

    See <a href='https://github.com/icfpcontest2020/aliens-proxy-protocol' target='_blank'>https://github.com/icfpcontest2020/aliens-proxy-protocol<a/>  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class GamesApiApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def games_game_id_get(self, game_id, **kwargs):  # noqa: E501
        """games_game_id_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.games_game_id_get(game_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str game_id: (required)
        :return: GameDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.games_game_id_get_with_http_info(game_id, **kwargs)  # noqa: E501
        else:
            (data) = self.games_game_id_get_with_http_info(game_id, **kwargs)  # noqa: E501
            return data

    def games_game_id_get_with_http_info(self, game_id, **kwargs):  # noqa: E501
        """games_game_id_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.games_game_id_get_with_http_info(game_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str game_id: (required)
        :return: GameDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['game_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method games_game_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'game_id' is set
        if ('game_id' not in params or
                params['game_id'] is None):
            raise ValueError("Missing the required parameter `game_id` when calling `games_game_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'game_id' in params:
            path_params['gameId'] = params['game_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ICFPC-ApiKey']  # noqa: E501

        return self.api_client.call_api(
            '/games/{gameId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GameDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def games_get(self, tournament_id, **kwargs):  # noqa: E501
        """games_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.games_get(tournament_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int tournament_id: (required)
        :param int take:
        :param datetime before:
        :return: GamesListDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.games_get_with_http_info(tournament_id, **kwargs)  # noqa: E501
        else:
            (data) = self.games_get_with_http_info(tournament_id, **kwargs)  # noqa: E501
            return data

    def games_get_with_http_info(self, tournament_id, **kwargs):  # noqa: E501
        """games_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.games_get_with_http_info(tournament_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int tournament_id: (required)
        :param int take:
        :param datetime before:
        :return: GamesListDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tournament_id', 'take', 'before']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method games_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'tournament_id' is set
        if ('tournament_id' not in params or
                params['tournament_id'] is None):
            raise ValueError("Missing the required parameter `tournament_id` when calling `games_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'tournament_id' in params:
            query_params.append(('tournamentId', params['tournament_id']))  # noqa: E501
        if 'take' in params:
            query_params.append(('take', params['take']))  # noqa: E501
        if 'before' in params:
            query_params.append(('before', params['before']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ICFPC-ApiKey']  # noqa: E501

        return self.api_client.call_api(
            '/games', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GamesListDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def games_non_rating_get(self, **kwargs):  # noqa: E501
        """games_non_rating_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.games_non_rating_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int take:
        :param datetime before:
        :return: GamesListDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.games_non_rating_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.games_non_rating_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def games_non_rating_get_with_http_info(self, **kwargs):  # noqa: E501
        """games_non_rating_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.games_non_rating_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int take:
        :param datetime before:
        :return: GamesListDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['take', 'before']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method games_non_rating_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'take' in params:
            query_params.append(('take', params['take']))  # noqa: E501
        if 'before' in params:
            query_params.append(('before', params['before']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ICFPC-ApiKey']  # noqa: E501

        return self.api_client.call_api(
            '/games/non-rating', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GamesListDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def games_non_rating_run_post(self, attacker_submission_id, defender_submission_id, **kwargs):  # noqa: E501
        """games_non_rating_run_post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.games_non_rating_run_post(attacker_submission_id, defender_submission_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int attacker_submission_id: (required)
        :param int defender_submission_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.games_non_rating_run_post_with_http_info(attacker_submission_id, defender_submission_id, **kwargs)  # noqa: E501
        else:
            (data) = self.games_non_rating_run_post_with_http_info(attacker_submission_id, defender_submission_id, **kwargs)  # noqa: E501
            return data

    def games_non_rating_run_post_with_http_info(self, attacker_submission_id, defender_submission_id, **kwargs):  # noqa: E501
        """games_non_rating_run_post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.games_non_rating_run_post_with_http_info(attacker_submission_id, defender_submission_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int attacker_submission_id: (required)
        :param int defender_submission_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['attacker_submission_id', 'defender_submission_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method games_non_rating_run_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'attacker_submission_id' is set
        if ('attacker_submission_id' not in params or
                params['attacker_submission_id'] is None):
            raise ValueError("Missing the required parameter `attacker_submission_id` when calling `games_non_rating_run_post`")  # noqa: E501
        # verify the required parameter 'defender_submission_id' is set
        if ('defender_submission_id' not in params or
                params['defender_submission_id'] is None):
            raise ValueError("Missing the required parameter `defender_submission_id` when calling `games_non_rating_run_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'attacker_submission_id' in params:
            query_params.append(('attackerSubmissionId', params['attacker_submission_id']))  # noqa: E501
        if 'defender_submission_id' in params:
            query_params.append(('defenderSubmissionId', params['defender_submission_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['ICFPC-ApiKey']  # noqa: E501

        return self.api_client.call_api(
            '/games/non-rating/run', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)