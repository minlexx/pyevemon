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


class GetUniverseMoonsMoonIdPosition(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, x=None, y=None, z=None):
        """
        GetUniverseMoonsMoonIdPosition - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'x': 'float',
            'y': 'float',
            'z': 'float'
        }

        self.attribute_map = {
            'x': 'x',
            'y': 'y',
            'z': 'z'
        }

        self._x = x
        self._y = y
        self._z = z

    @property
    def x(self):
        """
        Gets the x of this GetUniverseMoonsMoonIdPosition.
        x number

        :return: The x of this GetUniverseMoonsMoonIdPosition.
        :rtype: float
        """
        return self._x

    @x.setter
    def x(self, x):
        """
        Sets the x of this GetUniverseMoonsMoonIdPosition.
        x number

        :param x: The x of this GetUniverseMoonsMoonIdPosition.
        :type: float
        """
        if x is None:
            raise ValueError("Invalid value for `x`, must not be `None`")

        self._x = x

    @property
    def y(self):
        """
        Gets the y of this GetUniverseMoonsMoonIdPosition.
        y number

        :return: The y of this GetUniverseMoonsMoonIdPosition.
        :rtype: float
        """
        return self._y

    @y.setter
    def y(self, y):
        """
        Sets the y of this GetUniverseMoonsMoonIdPosition.
        y number

        :param y: The y of this GetUniverseMoonsMoonIdPosition.
        :type: float
        """
        if y is None:
            raise ValueError("Invalid value for `y`, must not be `None`")

        self._y = y

    @property
    def z(self):
        """
        Gets the z of this GetUniverseMoonsMoonIdPosition.
        z number

        :return: The z of this GetUniverseMoonsMoonIdPosition.
        :rtype: float
        """
        return self._z

    @z.setter
    def z(self, z):
        """
        Sets the z of this GetUniverseMoonsMoonIdPosition.
        z number

        :param z: The z of this GetUniverseMoonsMoonIdPosition.
        :type: float
        """
        if z is None:
            raise ValueError("Invalid value for `z`, must not be `None`")

        self._z = z

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
        if not isinstance(other, GetUniverseMoonsMoonIdPosition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
