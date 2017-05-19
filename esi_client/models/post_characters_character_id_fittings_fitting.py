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


class PostCharactersCharacterIdFittingsFitting(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, description=None, items=None, name=None, ship_type_id=None):
        """
        PostCharactersCharacterIdFittingsFitting - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'description': 'str',
            'items': 'list[PostCharactersCharacterIdFittingsItem]',
            'name': 'str',
            'ship_type_id': 'int'
        }

        self.attribute_map = {
            'description': 'description',
            'items': 'items',
            'name': 'name',
            'ship_type_id': 'ship_type_id'
        }

        self._description = description
        self._items = items
        self._name = name
        self._ship_type_id = ship_type_id

    @property
    def description(self):
        """
        Gets the description of this PostCharactersCharacterIdFittingsFitting.
        description string

        :return: The description of this PostCharactersCharacterIdFittingsFitting.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this PostCharactersCharacterIdFittingsFitting.
        description string

        :param description: The description of this PostCharactersCharacterIdFittingsFitting.
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")
        if description is not None and len(description) > 500:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `500`")
        if description is not None and len(description) < 0:
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")

        self._description = description

    @property
    def items(self):
        """
        Gets the items of this PostCharactersCharacterIdFittingsFitting.
        items array

        :return: The items of this PostCharactersCharacterIdFittingsFitting.
        :rtype: list[PostCharactersCharacterIdFittingsItem]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this PostCharactersCharacterIdFittingsFitting.
        items array

        :param items: The items of this PostCharactersCharacterIdFittingsFitting.
        :type: list[PostCharactersCharacterIdFittingsItem]
        """
        if items is None:
            raise ValueError("Invalid value for `items`, must not be `None`")

        self._items = items

    @property
    def name(self):
        """
        Gets the name of this PostCharactersCharacterIdFittingsFitting.
        name string

        :return: The name of this PostCharactersCharacterIdFittingsFitting.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this PostCharactersCharacterIdFittingsFitting.
        name string

        :param name: The name of this PostCharactersCharacterIdFittingsFitting.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")
        if name is not None and len(name) > 50:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `50`")
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")

        self._name = name

    @property
    def ship_type_id(self):
        """
        Gets the ship_type_id of this PostCharactersCharacterIdFittingsFitting.
        ship_type_id integer

        :return: The ship_type_id of this PostCharactersCharacterIdFittingsFitting.
        :rtype: int
        """
        return self._ship_type_id

    @ship_type_id.setter
    def ship_type_id(self, ship_type_id):
        """
        Sets the ship_type_id of this PostCharactersCharacterIdFittingsFitting.
        ship_type_id integer

        :param ship_type_id: The ship_type_id of this PostCharactersCharacterIdFittingsFitting.
        :type: int
        """
        if ship_type_id is None:
            raise ValueError("Invalid value for `ship_type_id`, must not be `None`")

        self._ship_type_id = ship_type_id

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
        if not isinstance(other, PostCharactersCharacterIdFittingsFitting):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
