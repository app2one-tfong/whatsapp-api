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


class GroupParticipantAction(ModelNormal):
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
        'group_id': 'groupId',  # noqa: E501
        'participant_chat_id': 'participantChatId',  # noqa: E501
        'participant_phone': 'participantPhone'  # noqa: E501
    }

    openapi_types = {
        'group_id': 'str',
        'participant_chat_id': 'str',
        'participant_phone': 'int'
    }

    validations = {
    }

    def __init__(self, group_id=None, participant_chat_id=None, participant_phone=None):  # noqa: E501
        """GroupParticipantAction - a model defined in OpenAPI"""  # noqa: E501

        self._group_id = None
        self._participant_chat_id = None
        self._participant_phone = None
        self.discriminator = None

        self.group_id = group_id
        self.participant_chat_id = participant_chat_id
        if participant_phone is not None:
            self.participant_phone = (
                participant_phone
            )

    @property
    def group_id(self):
        """Gets the group_id of this GroupParticipantAction.  # noqa: E501

        Chat ID from the chat list. Examples: 19680561234-1479621234@g.us for the group.  # noqa: E501

        :return: The group_id of this GroupParticipantAction.  # noqa: E501
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):  # noqa: E501
        """Sets the group_id of this GroupParticipantAction.

        Chat ID from the chat list. Examples: 19680561234-1479621234@g.us for the group.  # noqa: E501

        :param group_id: The group_id of this GroupParticipantAction.  # noqa: E501
        :type: str
        """
        if group_id is None:
            raise ApiValueError("Invalid value for `group_id`, must not be `None`")  # noqa: E501

        self._group_id = (
            group_id
        )

    @property
    def participant_chat_id(self):
        """Gets the participant_chat_id of this GroupParticipantAction.  # noqa: E501

        **Required if participantPhone is not set**  Chat ID from the message list. Examples: 17633123456@c.us. Used instead of the participantPhone parameter.  # noqa: E501

        :return: The participant_chat_id of this GroupParticipantAction.  # noqa: E501
        :rtype: str
        """
        return self._participant_chat_id

    @participant_chat_id.setter
    def participant_chat_id(self, participant_chat_id):  # noqa: E501
        """Sets the participant_chat_id of this GroupParticipantAction.

        **Required if participantPhone is not set**  Chat ID from the message list. Examples: 17633123456@c.us. Used instead of the participantPhone parameter.  # noqa: E501

        :param participant_chat_id: The participant_chat_id of this GroupParticipantAction.  # noqa: E501
        :type: str
        """
        if participant_chat_id is None:
            raise ApiValueError("Invalid value for `participant_chat_id`, must not be `None`")  # noqa: E501

        self._participant_chat_id = (
            participant_chat_id
        )

    @property
    def participant_phone(self):
        """Gets the participant_phone of this GroupParticipantAction.  # noqa: E501

        **Required if participantChatId is not set**  A phone number starting with the country code. You do not need to add your number.   USA example: 17472822486.  # noqa: E501

        :return: The participant_phone of this GroupParticipantAction.  # noqa: E501
        :rtype: int
        """
        return self._participant_phone

    @participant_phone.setter
    def participant_phone(self, participant_phone):  # noqa: E501
        """Sets the participant_phone of this GroupParticipantAction.

        **Required if participantChatId is not set**  A phone number starting with the country code. You do not need to add your number.   USA example: 17472822486.  # noqa: E501

        :param participant_phone: The participant_phone of this GroupParticipantAction.  # noqa: E501
        :type: int
        """

        self._participant_phone = (
            participant_phone
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
        if not isinstance(other, GroupParticipantAction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
