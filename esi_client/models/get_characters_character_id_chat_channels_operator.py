# coding: utf-8

"""
    EVE Swagger Interface

    An OpenAPI for EVE Online

    OpenAPI spec version: 0.4.6
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class GetCharactersCharacterIdChatChannelsOperator(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, accessor_id=None, accessor_type=None):
        """
        GetCharactersCharacterIdChatChannelsOperator - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'accessor_id': 'int',
            'accessor_type': 'str'
        }

        self.attribute_map = {
            'accessor_id': 'accessor_id',
            'accessor_type': 'accessor_type'
        }

        self._accessor_id = accessor_id
        self._accessor_type = accessor_type

    @property
    def accessor_id(self):
        """
        Gets the accessor_id of this GetCharactersCharacterIdChatChannelsOperator.
        ID of a channel operator

        :return: The accessor_id of this GetCharactersCharacterIdChatChannelsOperator.
        :rtype: int
        """
        return self._accessor_id

    @accessor_id.setter
    def accessor_id(self, accessor_id):
        """
        Sets the accessor_id of this GetCharactersCharacterIdChatChannelsOperator.
        ID of a channel operator

        :param accessor_id: The accessor_id of this GetCharactersCharacterIdChatChannelsOperator.
        :type: int
        """
        if accessor_id is None:
            raise ValueError("Invalid value for `accessor_id`, must not be `None`")

        self._accessor_id = accessor_id

    @property
    def accessor_type(self):
        """
        Gets the accessor_type of this GetCharactersCharacterIdChatChannelsOperator.
        accessor_type string

        :return: The accessor_type of this GetCharactersCharacterIdChatChannelsOperator.
        :rtype: str
        """
        return self._accessor_type

    @accessor_type.setter
    def accessor_type(self, accessor_type):
        """
        Sets the accessor_type of this GetCharactersCharacterIdChatChannelsOperator.
        accessor_type string

        :param accessor_type: The accessor_type of this GetCharactersCharacterIdChatChannelsOperator.
        :type: str
        """
        allowed_values = ["character", "corporation", "alliance"]
        if accessor_type not in allowed_values:
            raise ValueError(
                "Invalid value for `accessor_type` ({0}), must be one of {1}"
                .format(accessor_type, allowed_values)
            )

        self._accessor_type = accessor_type

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, GetCharactersCharacterIdChatChannelsOperator):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
