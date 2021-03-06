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


class GetUniverseCategoriesCategoryIdOk(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, category_id=None, groups=None, name=None, published=None):
        """
        GetUniverseCategoriesCategoryIdOk - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'category_id': 'int',
            'groups': 'list[int]',
            'name': 'str',
            'published': 'bool'
        }

        self.attribute_map = {
            'category_id': 'category_id',
            'groups': 'groups',
            'name': 'name',
            'published': 'published'
        }

        self._category_id = category_id
        self._groups = groups
        self._name = name
        self._published = published

    @property
    def category_id(self):
        """
        Gets the category_id of this GetUniverseCategoriesCategoryIdOk.
        category_id integer

        :return: The category_id of this GetUniverseCategoriesCategoryIdOk.
        :rtype: int
        """
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        """
        Sets the category_id of this GetUniverseCategoriesCategoryIdOk.
        category_id integer

        :param category_id: The category_id of this GetUniverseCategoriesCategoryIdOk.
        :type: int
        """
        if category_id is None:
            raise ValueError("Invalid value for `category_id`, must not be `None`")

        self._category_id = category_id

    @property
    def groups(self):
        """
        Gets the groups of this GetUniverseCategoriesCategoryIdOk.
        groups array

        :return: The groups of this GetUniverseCategoriesCategoryIdOk.
        :rtype: list[int]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """
        Sets the groups of this GetUniverseCategoriesCategoryIdOk.
        groups array

        :param groups: The groups of this GetUniverseCategoriesCategoryIdOk.
        :type: list[int]
        """
        if groups is None:
            raise ValueError("Invalid value for `groups`, must not be `None`")

        self._groups = groups

    @property
    def name(self):
        """
        Gets the name of this GetUniverseCategoriesCategoryIdOk.
        name string

        :return: The name of this GetUniverseCategoriesCategoryIdOk.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this GetUniverseCategoriesCategoryIdOk.
        name string

        :param name: The name of this GetUniverseCategoriesCategoryIdOk.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def published(self):
        """
        Gets the published of this GetUniverseCategoriesCategoryIdOk.
        published boolean

        :return: The published of this GetUniverseCategoriesCategoryIdOk.
        :rtype: bool
        """
        return self._published

    @published.setter
    def published(self, published):
        """
        Sets the published of this GetUniverseCategoriesCategoryIdOk.
        published boolean

        :param published: The published of this GetUniverseCategoriesCategoryIdOk.
        :type: bool
        """
        if published is None:
            raise ValueError("Invalid value for `published`, must not be `None`")

        self._published = published

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
        if not isinstance(other, GetUniverseCategoriesCategoryIdOk):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
