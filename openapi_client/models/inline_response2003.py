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


class InlineResponse2003(ModelNormal):
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
        ('account_status',): {
            'SENT_TO_WHATSAPP': "Retry request sent to WhatsApp",
            'NOT_SENT_BECAUSE_REASON_DON&#39;T_EQUALS_&quot;SYNCING&quot;': "Retry request not sent because reason don't equals \"syncing\""
        },
    }

    attribute_map = {
        'account_status': 'accountStatus'  # noqa: E501
    }

    openapi_types = {
        'account_status': 'str'
    }

    validations = {
    }

    def __init__(self, account_status=None):  # noqa: E501
        """InlineResponse2003 - a model defined in OpenAPI"""  # noqa: E501

        self._account_status = None
        self.discriminator = None

        if account_status is not None:
            self.account_status = (
                account_status
            )

    @property
    def account_status(self):
        """Gets the account_status of this InlineResponse2003.  # noqa: E501

        Instance Status  # noqa: E501

        :return: The account_status of this InlineResponse2003.  # noqa: E501
        :rtype: str
        """
        return self._account_status

    @account_status.setter
    def account_status(self, account_status):  # noqa: E501
        """Sets the account_status of this InlineResponse2003.

        Instance Status  # noqa: E501

        :param account_status: The account_status of this InlineResponse2003.  # noqa: E501
        :type: str
        """
        check_allowed_values(
            self.allowed_values,
            ('account_status',),
            account_status,
            self.validations
        )

        self._account_status = (
            account_status
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
        if not isinstance(other, InlineResponse2003):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
