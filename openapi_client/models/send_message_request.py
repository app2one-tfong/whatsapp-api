# coding: utf-8

"""
    Chat API SDK

    The SDK allows you to receive and send messages through your WhatsApp account. [Sign up now](https://app.chat-api.com/)  The Chat API is based on the WhatsApp WEB protocol and excludes the ban both when using libraries from mgp25 and the like. Despite this, your account can be banned by anti-spam system WhatsApp after several clicking the \"block\" button.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: sale@chat-api.com
    Generated by: https://openapi-generator.tech
"""


import pprint  # noqa: F401
import re  # noqa: F401

import six  # noqa: F401

from openapi_client.exceptions import ApiValueError  # noqa: F401
from openapi_client.model_utils import (  # noqa: F401
    ModelNormal,
    ModelSimple,
    check_allowed_values,
    check_validations
)


class SendMessageRequest(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      openapi_types (dict): The key is attribute name
          and the value is attribute type.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
    """

    allowed_values = {
    }

    attribute_map = {
        'chat_id': 'chatId',  # noqa: E501
        'phone': 'phone',  # noqa: E501
        'body': 'body'  # noqa: E501
    }

    openapi_types = {
        'chat_id': 'str',
        'phone': 'int',
        'body': 'str'
    }

    validations = {
    }

    def __init__(self, chat_id=None, phone=None, body=None):  # noqa: E501
        """SendMessageRequest - a model defined in OpenAPI"""  # noqa: E501

        self._chat_id = None
        self._phone = None
        self._body = None
        self.discriminator = None

        if chat_id is not None:
            self.chat_id = (
                chat_id
            )
        if phone is not None:
            self.phone = (
                phone
            )
        self.body = body

    @property
    def chat_id(self):
        """Gets the chat_id of this SendMessageRequest.  # noqa: E501

        **Required if phone is not set**  Chat ID from the message list. Examples: 17633123456@c.us for private messages and 17680561234-1479621234@g.us for the group. Used instead of the phone parameter.  # noqa: E501

        :return: The chat_id of this SendMessageRequest.  # noqa: E501
        :rtype: str
        """
        return self._chat_id

    @chat_id.setter
    def chat_id(self, chat_id):  # noqa: E501
        """Sets the chat_id of this SendMessageRequest.

        **Required if phone is not set**  Chat ID from the message list. Examples: 17633123456@c.us for private messages and 17680561234-1479621234@g.us for the group. Used instead of the phone parameter.  # noqa: E501

        :param chat_id: The chat_id of this SendMessageRequest.  # noqa: E501
        :type: str
        """

        self._chat_id = (
            chat_id
        )

    @property
    def phone(self):
        """Gets the phone of this SendMessageRequest.  # noqa: E501

        **Required if chatId is not set**  A phone number starting with the country code. You do not need to add your number.   USA example: 17472822486.  # noqa: E501

        :return: The phone of this SendMessageRequest.  # noqa: E501
        :rtype: int
        """
        return self._phone

    @phone.setter
    def phone(self, phone):  # noqa: E501
        """Sets the phone of this SendMessageRequest.

        **Required if chatId is not set**  A phone number starting with the country code. You do not need to add your number.   USA example: 17472822486.  # noqa: E501

        :param phone: The phone of this SendMessageRequest.  # noqa: E501
        :type: int
        """

        self._phone = (
            phone
        )

    @property
    def body(self):
        """Gets the body of this SendMessageRequest.  # noqa: E501

        Message text, UTF-8 or UTF-16 string with emoji 🍏  # noqa: E501

        :return: The body of this SendMessageRequest.  # noqa: E501
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):  # noqa: E501
        """Sets the body of this SendMessageRequest.

        Message text, UTF-8 or UTF-16 string with emoji 🍏  # noqa: E501

        :param body: The body of this SendMessageRequest.  # noqa: E501
        :type: str
        """
        if body is None:
            raise ApiValueError("Invalid value for `body`, must not be `None`")  # noqa: E501

        self._body = (
            body
        )

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SendMessageRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
