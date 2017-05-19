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


class GetCharactersCharacterIdClonesHomeLocation(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, location_id=None, location_type=None):
        """
        GetCharactersCharacterIdClonesHomeLocation - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'location_id': 'int',
            'location_type': 'str'
        }

        self.attribute_map = {
            'location_id': 'location_id',
            'location_type': 'location_type'
        }

        self._location_id = location_id
        self._location_type = location_type

    @property
    def location_id(self):
        """
        Gets the location_id of this GetCharactersCharacterIdClonesHomeLocation.
        location_id integer

        :return: The location_id of this GetCharactersCharacterIdClonesHomeLocation.
        :rtype: int
        """
        return self._location_id

    @location_id.setter
    def location_id(self, location_id):
        """
        Sets the location_id of this GetCharactersCharacterIdClonesHomeLocation.
        location_id integer

        :param location_id: The location_id of this GetCharactersCharacterIdClonesHomeLocation.
        :type: int
        """

        self._location_id = location_id

    @property
    def location_type(self):
        """
        Gets the location_type of this GetCharactersCharacterIdClonesHomeLocation.
        location_type string

        :return: The location_type of this GetCharactersCharacterIdClonesHomeLocation.
        :rtype: str
        """
        return self._location_type

    @location_type.setter
    def location_type(self, location_type):
        """
        Sets the location_type of this GetCharactersCharacterIdClonesHomeLocation.
        location_type string

        :param location_type: The location_type of this GetCharactersCharacterIdClonesHomeLocation.
        :type: str
        """
        allowed_values = ["station", "structure"]
        if location_type not in allowed_values:
            raise ValueError(
                "Invalid value for `location_type` ({0}), must be one of {1}"
                .format(location_type, allowed_values)
            )

        self._location_type = location_type

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
        if not isinstance(other, GetCharactersCharacterIdClonesHomeLocation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
