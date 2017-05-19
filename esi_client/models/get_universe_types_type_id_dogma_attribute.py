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


class GetUniverseTypesTypeIdDogmaAttribute(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, attribute_id=None, value=None):
        """
        GetUniverseTypesTypeIdDogmaAttribute - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'attribute_id': 'int',
            'value': 'float'
        }

        self.attribute_map = {
            'attribute_id': 'attribute_id',
            'value': 'value'
        }

        self._attribute_id = attribute_id
        self._value = value

    @property
    def attribute_id(self):
        """
        Gets the attribute_id of this GetUniverseTypesTypeIdDogmaAttribute.
        attribute_id integer

        :return: The attribute_id of this GetUniverseTypesTypeIdDogmaAttribute.
        :rtype: int
        """
        return self._attribute_id

    @attribute_id.setter
    def attribute_id(self, attribute_id):
        """
        Sets the attribute_id of this GetUniverseTypesTypeIdDogmaAttribute.
        attribute_id integer

        :param attribute_id: The attribute_id of this GetUniverseTypesTypeIdDogmaAttribute.
        :type: int
        """
        if attribute_id is None:
            raise ValueError("Invalid value for `attribute_id`, must not be `None`")

        self._attribute_id = attribute_id

    @property
    def value(self):
        """
        Gets the value of this GetUniverseTypesTypeIdDogmaAttribute.
        value number

        :return: The value of this GetUniverseTypesTypeIdDogmaAttribute.
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this GetUniverseTypesTypeIdDogmaAttribute.
        value number

        :param value: The value of this GetUniverseTypesTypeIdDogmaAttribute.
        :type: float
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")

        self._value = value

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
        if not isinstance(other, GetUniverseTypesTypeIdDogmaAttribute):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
