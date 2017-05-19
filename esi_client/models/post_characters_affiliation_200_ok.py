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


class PostCharactersAffiliation200Ok(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, alliance_id=None, character_id=None, corporation_id=None, faction_id=None):
        """
        PostCharactersAffiliation200Ok - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'alliance_id': 'int',
            'character_id': 'int',
            'corporation_id': 'int',
            'faction_id': 'int'
        }

        self.attribute_map = {
            'alliance_id': 'alliance_id',
            'character_id': 'character_id',
            'corporation_id': 'corporation_id',
            'faction_id': 'faction_id'
        }

        self._alliance_id = alliance_id
        self._character_id = character_id
        self._corporation_id = corporation_id
        self._faction_id = faction_id

    @property
    def alliance_id(self):
        """
        Gets the alliance_id of this PostCharactersAffiliation200Ok.
        The character's alliance ID, if their corporation is in an alliance

        :return: The alliance_id of this PostCharactersAffiliation200Ok.
        :rtype: int
        """
        return self._alliance_id

    @alliance_id.setter
    def alliance_id(self, alliance_id):
        """
        Sets the alliance_id of this PostCharactersAffiliation200Ok.
        The character's alliance ID, if their corporation is in an alliance

        :param alliance_id: The alliance_id of this PostCharactersAffiliation200Ok.
        :type: int
        """

        self._alliance_id = alliance_id

    @property
    def character_id(self):
        """
        Gets the character_id of this PostCharactersAffiliation200Ok.
        The character's ID

        :return: The character_id of this PostCharactersAffiliation200Ok.
        :rtype: int
        """
        return self._character_id

    @character_id.setter
    def character_id(self, character_id):
        """
        Sets the character_id of this PostCharactersAffiliation200Ok.
        The character's ID

        :param character_id: The character_id of this PostCharactersAffiliation200Ok.
        :type: int
        """
        if character_id is None:
            raise ValueError("Invalid value for `character_id`, must not be `None`")

        self._character_id = character_id

    @property
    def corporation_id(self):
        """
        Gets the corporation_id of this PostCharactersAffiliation200Ok.
        The character's corporation ID

        :return: The corporation_id of this PostCharactersAffiliation200Ok.
        :rtype: int
        """
        return self._corporation_id

    @corporation_id.setter
    def corporation_id(self, corporation_id):
        """
        Sets the corporation_id of this PostCharactersAffiliation200Ok.
        The character's corporation ID

        :param corporation_id: The corporation_id of this PostCharactersAffiliation200Ok.
        :type: int
        """
        if corporation_id is None:
            raise ValueError("Invalid value for `corporation_id`, must not be `None`")

        self._corporation_id = corporation_id

    @property
    def faction_id(self):
        """
        Gets the faction_id of this PostCharactersAffiliation200Ok.
        The character's faction ID, if their corporation is in a faction

        :return: The faction_id of this PostCharactersAffiliation200Ok.
        :rtype: int
        """
        return self._faction_id

    @faction_id.setter
    def faction_id(self, faction_id):
        """
        Sets the faction_id of this PostCharactersAffiliation200Ok.
        The character's faction ID, if their corporation is in a faction

        :param faction_id: The faction_id of this PostCharactersAffiliation200Ok.
        :type: int
        """

        self._faction_id = faction_id

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
        if not isinstance(other, PostCharactersAffiliation200Ok):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other