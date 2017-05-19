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


class GetUniverseGroupsGroupIdOk(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, category_id=None, group_id=None, name=None, published=None, types=None):
        """
        GetUniverseGroupsGroupIdOk - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'category_id': 'int',
            'group_id': 'int',
            'name': 'str',
            'published': 'bool',
            'types': 'list[int]'
        }

        self.attribute_map = {
            'category_id': 'category_id',
            'group_id': 'group_id',
            'name': 'name',
            'published': 'published',
            'types': 'types'
        }

        self._category_id = category_id
        self._group_id = group_id
        self._name = name
        self._published = published
        self._types = types

    @property
    def category_id(self):
        """
        Gets the category_id of this GetUniverseGroupsGroupIdOk.
        category_id integer

        :return: The category_id of this GetUniverseGroupsGroupIdOk.
        :rtype: int
        """
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        """
        Sets the category_id of this GetUniverseGroupsGroupIdOk.
        category_id integer

        :param category_id: The category_id of this GetUniverseGroupsGroupIdOk.
        :type: int
        """
        if category_id is None:
            raise ValueError("Invalid value for `category_id`, must not be `None`")

        self._category_id = category_id

    @property
    def group_id(self):
        """
        Gets the group_id of this GetUniverseGroupsGroupIdOk.
        group_id integer

        :return: The group_id of this GetUniverseGroupsGroupIdOk.
        :rtype: int
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """
        Sets the group_id of this GetUniverseGroupsGroupIdOk.
        group_id integer

        :param group_id: The group_id of this GetUniverseGroupsGroupIdOk.
        :type: int
        """
        if group_id is None:
            raise ValueError("Invalid value for `group_id`, must not be `None`")

        self._group_id = group_id

    @property
    def name(self):
        """
        Gets the name of this GetUniverseGroupsGroupIdOk.
        name string

        :return: The name of this GetUniverseGroupsGroupIdOk.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this GetUniverseGroupsGroupIdOk.
        name string

        :param name: The name of this GetUniverseGroupsGroupIdOk.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def published(self):
        """
        Gets the published of this GetUniverseGroupsGroupIdOk.
        published boolean

        :return: The published of this GetUniverseGroupsGroupIdOk.
        :rtype: bool
        """
        return self._published

    @published.setter
    def published(self, published):
        """
        Sets the published of this GetUniverseGroupsGroupIdOk.
        published boolean

        :param published: The published of this GetUniverseGroupsGroupIdOk.
        :type: bool
        """
        if published is None:
            raise ValueError("Invalid value for `published`, must not be `None`")

        self._published = published

    @property
    def types(self):
        """
        Gets the types of this GetUniverseGroupsGroupIdOk.
        types array

        :return: The types of this GetUniverseGroupsGroupIdOk.
        :rtype: list[int]
        """
        return self._types

    @types.setter
    def types(self, types):
        """
        Sets the types of this GetUniverseGroupsGroupIdOk.
        types array

        :param types: The types of this GetUniverseGroupsGroupIdOk.
        :type: list[int]
        """
        if types is None:
            raise ValueError("Invalid value for `types`, must not be `None`")

        self._types = types

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
        if not isinstance(other, GetUniverseGroupsGroupIdOk):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other