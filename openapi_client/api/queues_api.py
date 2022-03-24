# coding: utf-8

"""
    Chat API SDK

    The SDK allows you to receive and send messages through your WhatsApp account. [Sign up now](https://app.chat-api.com/)  The Chat API is based on the WhatsApp WEB protocol and excludes the ban both when using libraries from mgp25 and the like. Despite this, your account can be banned by anti-spam system WhatsApp after several clicking the \"block\" button.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: sale@chat-api.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from openapi_client.api_client import ApiClient
from openapi_client.exceptions import (
    ApiTypeError,
    ApiValueError
)
from openapi_client.model_utils import (
    check_allowed_values,
    check_validations
)


class QueuesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __clear_actions_queue(self, **kwargs):  # noqa: E501
            """Clear outbound actions queue.  # noqa: E501

            This method is needed when you accidentally sent thousands of actions in a row.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True
            >>> thread = api.clear_actions_queue(async_req=True)
            >>> result = thread.get()

            :param async_req bool: execute request asynchronously
            :param _return_http_data_only: response data without head status
                code and headers
            :param _preload_content: if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            :param _request_timeout: timeout setting for this request. If one
                number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
            :return: ClearActionsQueueStatus
                If the method is called asynchronously, returns the request
                thread.
            """
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            return self.call_with_http_info(**kwargs)

        self.clear_actions_queue = Endpoint(
            settings={
                'response_type': 'ClearActionsQueueStatus',
                'auth': [
                    'instanceId', 
                    'token'
                ],
                'endpoint_path': '/clearActionsQueue',
                'operation_id': 'clear_actions_queue',
                'http_method': 'POST',
                'servers': [],
            },
            params_map={
                'all': [
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                },
                'attribute_map': {
                },
                'location_map': {
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__clear_actions_queue
        )

        def __clear_messages_queue(self, **kwargs):  # noqa: E501
            """Clear outbound messages queue.  # noqa: E501

            This method is needed when you accidentally sent thousands of messages in a row.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True
            >>> thread = api.clear_messages_queue(async_req=True)
            >>> result = thread.get()

            :param async_req bool: execute request asynchronously
            :param _return_http_data_only: response data without head status
                code and headers
            :param _preload_content: if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            :param _request_timeout: timeout setting for this request. If one
                number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
            :return: ClearMessagesQueueStatus
                If the method is called asynchronously, returns the request
                thread.
            """
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            return self.call_with_http_info(**kwargs)

        self.clear_messages_queue = Endpoint(
            settings={
                'response_type': 'ClearMessagesQueueStatus',
                'auth': [
                    'instanceId', 
                    'token'
                ],
                'endpoint_path': '/clearMessagesQueue',
                'operation_id': 'clear_messages_queue',
                'http_method': 'POST',
                'servers': [],
            },
            params_map={
                'all': [
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                },
                'attribute_map': {
                },
                'location_map': {
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__clear_messages_queue
        )

        def __show_actions_queue(self, **kwargs):  # noqa: E501
            """Get outbound messages queue.  # noqa: E501

            When you create an action, all actions are queued up. If an action is not executed, it remains in the queue and will be sent for execution in time. again. The action cannot be executed due to the status of the device connected to the account.  This method give the last 100 actions in the queue.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True
            >>> thread = api.show_actions_queue(async_req=True)
            >>> result = thread.get()

            :param async_req bool: execute request asynchronously
            :param _return_http_data_only: response data without head status
                code and headers
            :param _preload_content: if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            :param _request_timeout: timeout setting for this request. If one
                number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
            :return: OutboundActions
                If the method is called asynchronously, returns the request
                thread.
            """
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            return self.call_with_http_info(**kwargs)

        self.show_actions_queue = Endpoint(
            settings={
                'response_type': 'OutboundActions',
                'auth': [
                    'instanceId', 
                    'token'
                ],
                'endpoint_path': '/showActionsQueue',
                'operation_id': 'show_actions_queue',
                'http_method': 'GET',
                'servers': [],
            },
            params_map={
                'all': [
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                },
                'attribute_map': {
                },
                'location_map': {
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__show_actions_queue
        )

        def __show_messages_queue(self, **kwargs):  # noqa: E501
            """Get outbound messages queue.  # noqa: E501

            When sending messages, all messages are in the queue. If the message is not sent, then it remains in the queue and in time it will be sent again. The message may not be sent due to the status of the device connected to the account.   This method give the last 100 messages in the queue.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True
            >>> thread = api.show_messages_queue(async_req=True)
            >>> result = thread.get()

            :param async_req bool: execute request asynchronously
            :param _return_http_data_only: response data without head status
                code and headers
            :param _preload_content: if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            :param _request_timeout: timeout setting for this request. If one
                number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
            :return: OutboundMessages
                If the method is called asynchronously, returns the request
                thread.
            """
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            return self.call_with_http_info(**kwargs)

        self.show_messages_queue = Endpoint(
            settings={
                'response_type': 'OutboundMessages',
                'auth': [
                    'instanceId', 
                    'token'
                ],
                'endpoint_path': '/showMessagesQueue',
                'operation_id': 'show_messages_queue',
                'http_method': 'GET',
                'servers': [],
            },
            params_map={
                'all': [
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                },
                'attribute_map': {
                },
                'location_map': {
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__show_messages_queue
        )


class Endpoint(object):
    def __init__(self, settings=None, params_map=None, root_map=None,
                 headers_map=None, api_client=None, callable=None):
        """Creates an endpoint

        Args:
            settings (dict): see below key value pairs
                'response_type' (str): response type
                'auth' (list): a list of auth type keys
                'endpoint_path' (str): the endpoint path
                'operation_id' (str): endpoint string identifier
                'http_method' (str): POST/PUT/PATCH/GET etc
                'servers' (list): list of str servers that this endpoint is at
            params_map (dict): see below key value pairs
                'all' (list): list of str endpoint parameter names
                'required' (list): list of required parameter names
                'nullable' (list): list of nullable parameter names
                'enum' (list): list of parameters with enum values
                'validation' (list): list of parameters with validations
            root_map
                'validations' (dict): the dict mapping endpoint parameter tuple
                    paths to their validation dictionaries
                'allowed_values' (dict): the dict mapping endpoint parameter
                    tuple paths to their allowed_values (enum) dictionaries
                'openapi_types' (dict): param_name to openapi type
                'attribute_map' (dict): param_name to camelCase name
                'location_map' (dict): param_name to  'body', 'file', 'form',
                    'header', 'path', 'query'
                collection_format_map (dict): param_name to `csv` etc.
            headers_map (dict): see below key value pairs
                'accept' (list): list of Accept header strings
                'content_type' (list): list of Content-Type header strings
            api_client (ApiClient) api client instance
            callable (function): the function which is invoked when the
                Endpoint is called
        """
        self.settings = settings
        self.params_map = params_map
        self.params_map['all'].extend([
            'async_req',
            '_host_index',
            '_preload_content',
            '_request_timeout',
            '_return_http_data_only'
        ])
        self.validations = root_map['validations']
        self.allowed_values = root_map['allowed_values']
        self.openapi_types = root_map['openapi_types']
        self.attribute_map = root_map['attribute_map']
        self.location_map = root_map['location_map']
        self.collection_format_map = root_map['collection_format_map']
        self.headers_map = headers_map
        self.api_client = api_client
        self.callable = callable

    def __validate_inputs(self, kwargs):
        for param in self.params_map['enum']:
            if param in kwargs:
                check_allowed_values(
                    self.allowed_values,
                    (param,),
                    kwargs[param],
                    self.validations
                )

        for param in self.params_map['validation']:
            if param in kwargs:
                check_validations(
                    self.validations,
                    (param,),
                    kwargs[param]
                )

    def __gather_params(self, kwargs):
        params = {
            'body': None,
            'collection_format': {},
            'file': {},
            'form': [],
            'header': {},
            'path': {},
            'query': []
        }

        for param_name, param_value in six.iteritems(kwargs):
            param_location = self.location_map.get(param_name)
            if param_location:
                if param_location == 'body':
                    params['body'] = param_value
                    continue
                base_name = self.attribute_map[param_name]
                if (param_location == 'form' and
                        self.openapi_types[param_name] == 'file'):
                    param_location = 'file'
                elif param_location in {'form', 'query'}:
                    param_value_full = (base_name, param_value)
                    params[param_location].append(param_value_full)
                if param_location not in {'form', 'query'}:
                    params[param_location][base_name] = param_value
                collection_format = self.collection_format_map.get(param_name)
                if collection_format:
                    params['collection_format'][base_name] = collection_format

        return params

    def __call__(self, *args, **kwargs):
        """ This method is invoked when endpoints are called
        Example:
        pet_api = PetApi()
        pet_api.add_pet  # this is an instance of the class Endpoint
        pet_api.add_pet()  # this invokes pet_api.add_pet.__call__()
        which then invokes the callable functions stored in that endpoint at
        pet_api.add_pet.callable or self.callable in this class
        """
        return self.callable(self, *args, **kwargs)

    def call_with_http_info(self, **kwargs):

        if kwargs.get('_host_index') and self.settings['servers']:
            _host_index = kwargs.get('_host_index')
            try:
                _host = self.settings['servers'][_host_index]
            except IndexError:
                raise ApiValueError(
                    "Invalid host index. Must be 0 <= index < %s" %
                    len(self.settings['servers'])
                )
        else:
            try:
                _host = self.settings['servers'][0]
            except IndexError:
                _host = None

        for key, value in six.iteritems(kwargs):
            if key not in self.params_map['all']:
                raise ApiTypeError(
                    "Got an unexpected parameter '%s'"
                    " to method `%s`" %
                    (key, self.settings['operation_id'])
                )
            if key not in self.params_map['nullable'] and value is None:
                raise ApiValueError(
                    "Value may not be None for non-nullable parameter `%s`"
                    " when calling `%s`" %
                    (key, self.settings['operation_id'])
                )

        for key in self.params_map['required']:
            if key not in kwargs.keys():
                raise ApiValueError(
                    "Missing the required parameter `%s` when calling "
                    "`%s`" % (key, self.settings['operation_id'])
                )

        self.__validate_inputs(kwargs)

        params = self.__gather_params(kwargs)

        accept_headers_list = self.headers_map['accept']
        if accept_headers_list:
            params['header']['Accept'] = self.api_client.select_header_accept(
                accept_headers_list)

        content_type_headers_list = self.headers_map['content_type']
        if content_type_headers_list:
            header_list = self.api_client.select_header_content_type(
                content_type_headers_list)
            params['header']['Content-Type'] = header_list

        return self.api_client.call_api(
            self.settings['endpoint_path'], self.settings['http_method'],
            params['path'],
            params['query'],
            params['header'],
            body=params['body'],
            post_params=params['form'],
            files=params['file'],
            response_type=self.settings['response_type'],
            auth_settings=self.settings['auth'],
            async_req=kwargs.get('async_req'),
            _return_http_data_only=kwargs.get('_return_http_data_only'),
            _preload_content=kwargs.get('_preload_content', True),
            _request_timeout=kwargs.get('_request_timeout'),
            _host=_host,
            collection_formats=params['collection_format'])
