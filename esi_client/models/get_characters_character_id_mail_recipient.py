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


class GetCharactersCharacterIdMailRecipient(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, recipient_id=None, recipient_type=None):
        """
        GetCharactersCharacterIdMailRecipient - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'recipient_id': 'int',
            'recipient_type': 'str'
        }

        self.attribute_map = {
            'recipient_id': 'recipient_id',
            'recipient_type': 'recipient_type'
        }

        self._recipient_id = recipient_id
        self._recipient_type = recipient_type

    @property
    def recipient_id(self):
        """
        Gets the recipient_id of this GetCharactersCharacterIdMailRecipient.
        recipient_id integer

        :return: The recipient_id of this GetCharactersCharacterIdMailRecipient.
        :rtype: int
        """
        return self._recipient_id

    @recipient_id.setter
    def recipient_id(self, recipient_id):
        """
        Sets the recipient_id of this GetCharactersCharacterIdMailRecipient.
        recipient_id integer

        :param recipient_id: The recipient_id of this GetCharactersCharacterIdMailRecipient.
        :type: int
        """
        if recipient_id is None:
            raise ValueError("Invalid value for `recipient_id`, must not be `None`")

        self._recipient_id = recipient_id

    @property
    def recipient_type(self):
        """
        Gets the recipient_type of this GetCharactersCharacterIdMailRecipient.
        recipient_type string

        :return: The recipient_type of this GetCharactersCharacterIdMailRecipient.
        :rtype: str
        """
        return self._recipient_type

    @recipient_type.setter
    def recipient_type(self, recipient_type):
        """
        Sets the recipient_type of this GetCharactersCharacterIdMailRecipient.
        recipient_type string

        :param recipient_type: The recipient_type of this GetCharactersCharacterIdMailRecipient.
        :type: str
        """
        allowed_values = ["alliance", "character", "corporation", "mailing_list"]
        if recipient_type not in allowed_values:
            raise ValueError(
                "Invalid value for `recipient_type` ({0}), must be one of {1}"
                .format(recipient_type, allowed_values)
            )

        self._recipient_type = recipient_type

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
        if not isinstance(other, GetCharactersCharacterIdMailRecipient):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
