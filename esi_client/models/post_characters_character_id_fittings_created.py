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


class PostCharactersCharacterIdFittingsCreated(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, fitting_id=None):
        """
        PostCharactersCharacterIdFittingsCreated - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'fitting_id': 'int'
        }

        self.attribute_map = {
            'fitting_id': 'fitting_id'
        }

        self._fitting_id = fitting_id

    @property
    def fitting_id(self):
        """
        Gets the fitting_id of this PostCharactersCharacterIdFittingsCreated.
        fitting_id integer

        :return: The fitting_id of this PostCharactersCharacterIdFittingsCreated.
        :rtype: int
        """
        return self._fitting_id

    @fitting_id.setter
    def fitting_id(self, fitting_id):
        """
        Sets the fitting_id of this PostCharactersCharacterIdFittingsCreated.
        fitting_id integer

        :param fitting_id: The fitting_id of this PostCharactersCharacterIdFittingsCreated.
        :type: int
        """
        if fitting_id is None:
            raise ValueError("Invalid value for `fitting_id`, must not be `None`")

        self._fitting_id = fitting_id

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
        if not isinstance(other, PostCharactersCharacterIdFittingsCreated):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other