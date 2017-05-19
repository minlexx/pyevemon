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


class GetUniversePlanetsPlanetIdOk(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, planet_id=None, position=None, system_id=None, type_id=None):
        """
        GetUniversePlanetsPlanetIdOk - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'planet_id': 'int',
            'position': 'GetUniversePlanetsPlanetIdPosition',
            'system_id': 'int',
            'type_id': 'int'
        }

        self.attribute_map = {
            'name': 'name',
            'planet_id': 'planet_id',
            'position': 'position',
            'system_id': 'system_id',
            'type_id': 'type_id'
        }

        self._name = name
        self._planet_id = planet_id
        self._position = position
        self._system_id = system_id
        self._type_id = type_id

    @property
    def name(self):
        """
        Gets the name of this GetUniversePlanetsPlanetIdOk.
        name string

        :return: The name of this GetUniversePlanetsPlanetIdOk.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this GetUniversePlanetsPlanetIdOk.
        name string

        :param name: The name of this GetUniversePlanetsPlanetIdOk.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def planet_id(self):
        """
        Gets the planet_id of this GetUniversePlanetsPlanetIdOk.
        planet_id integer

        :return: The planet_id of this GetUniversePlanetsPlanetIdOk.
        :rtype: int
        """
        return self._planet_id

    @planet_id.setter
    def planet_id(self, planet_id):
        """
        Sets the planet_id of this GetUniversePlanetsPlanetIdOk.
        planet_id integer

        :param planet_id: The planet_id of this GetUniversePlanetsPlanetIdOk.
        :type: int
        """
        if planet_id is None:
            raise ValueError("Invalid value for `planet_id`, must not be `None`")

        self._planet_id = planet_id

    @property
    def position(self):
        """
        Gets the position of this GetUniversePlanetsPlanetIdOk.

        :return: The position of this GetUniversePlanetsPlanetIdOk.
        :rtype: GetUniversePlanetsPlanetIdPosition
        """
        return self._position

    @position.setter
    def position(self, position):
        """
        Sets the position of this GetUniversePlanetsPlanetIdOk.

        :param position: The position of this GetUniversePlanetsPlanetIdOk.
        :type: GetUniversePlanetsPlanetIdPosition
        """

        self._position = position

    @property
    def system_id(self):
        """
        Gets the system_id of this GetUniversePlanetsPlanetIdOk.
        The solar system this planet is in

        :return: The system_id of this GetUniversePlanetsPlanetIdOk.
        :rtype: int
        """
        return self._system_id

    @system_id.setter
    def system_id(self, system_id):
        """
        Sets the system_id of this GetUniversePlanetsPlanetIdOk.
        The solar system this planet is in

        :param system_id: The system_id of this GetUniversePlanetsPlanetIdOk.
        :type: int
        """
        if system_id is None:
            raise ValueError("Invalid value for `system_id`, must not be `None`")

        self._system_id = system_id

    @property
    def type_id(self):
        """
        Gets the type_id of this GetUniversePlanetsPlanetIdOk.
        type_id integer

        :return: The type_id of this GetUniversePlanetsPlanetIdOk.
        :rtype: int
        """
        return self._type_id

    @type_id.setter
    def type_id(self, type_id):
        """
        Sets the type_id of this GetUniversePlanetsPlanetIdOk.
        type_id integer

        :param type_id: The type_id of this GetUniversePlanetsPlanetIdOk.
        :type: int
        """
        if type_id is None:
            raise ValueError("Invalid value for `type_id`, must not be `None`")

        self._type_id = type_id

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
        if not isinstance(other, GetUniversePlanetsPlanetIdOk):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
