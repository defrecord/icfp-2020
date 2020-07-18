# coding: utf-8

"""
    ICFP Contest 2020 API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class AliensApiApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def aliens_response_id_get(self, response_id, **kwargs):  # noqa: E501
        """aliens_response_id_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.aliens_response_id_get(response_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str response_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.aliens_response_id_get_with_http_info(response_id, **kwargs)  # noqa: E501
        else:
            (data) = self.aliens_response_id_get_with_http_info(response_id, **kwargs)  # noqa: E501
            return data

    def aliens_response_id_get_with_http_info(self, response_id, **kwargs):  # noqa: E501
        """aliens_response_id_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.aliens_response_id_get_with_http_info(response_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str response_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['response_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method aliens_response_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'response_id' is set
        if ('response_id' not in params or
                params['response_id'] is None):
            raise ValueError("Missing the required parameter `response_id` when calling `aliens_response_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'response_id' in params:
            path_params['responseId'] = params['response_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['ICFPC-ApiKey']  # noqa: E501

        return self.api_client.call_api(
            '/aliens/{responseId}', 'GET',
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

    def aliens_send_post(self, **kwargs):  # noqa: E501
        """aliens_send_post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.aliens_send_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.aliens_send_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.aliens_send_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def aliens_send_post_with_http_info(self, **kwargs):  # noqa: E501
        """aliens_send_post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.aliens_send_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method aliens_send_post" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['text/plain'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ICFPC-ApiKey']  # noqa: E501

        return self.api_client.call_api(
            '/aliens/send', 'POST',
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