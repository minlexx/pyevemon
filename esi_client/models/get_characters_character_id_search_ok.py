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


class GetCharactersCharacterIdSearchOk(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, agent=None, alliance=None, character=None, constellation=None, corporation=None, faction=None, inventorytype=None, region=None, solarsystem=None, station=None, structure=None, wormhole=None):
        """
        GetCharactersCharacterIdSearchOk - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'agent': 'list[int]',
            'alliance': 'list[int]',
            'character': 'list[int]',
            'constellation': 'list[int]',
            'corporation': 'list[int]',
            'faction': 'list[int]',
            'inventorytype': 'list[int]',
            'region': 'list[int]',
            'solarsystem': 'list[int]',
            'station': 'list[int]',
            'structure': 'list[int]',
            'wormhole': 'list[int]'
        }

        self.attribute_map = {
            'agent': 'agent',
            'alliance': 'alliance',
            'character': 'character',
            'constellation': 'constellation',
            'corporation': 'corporation',
            'faction': 'faction',
            'inventorytype': 'inventorytype',
            'region': 'region',
            'solarsystem': 'solarsystem',
            'station': 'station',
            'structure': 'structure',
            'wormhole': 'wormhole'
        }

        self._agent = agent
        self._alliance = alliance
        self._character = character
        self._constellation = constellation
        self._corporation = corporation
        self._faction = faction
        self._inventorytype = inventorytype
        self._region = region
        self._solarsystem = solarsystem
        self._station = station
        self._structure = structure
        self._wormhole = wormhole

    @property
    def agent(self):
        """
        Gets the agent of this GetCharactersCharacterIdSearchOk.
        agent array

        :return: The agent of this GetCharactersCharacterIdSearchOk.
        :rtype: list[int]
        """
        return self._agent

    @agent.setter
    def agent(self, agent):
        """
        Sets the agent of this GetCharactersCharacterIdSearchOk.
        agent array

        :param agent: The agent of this GetCharactersCharacterIdSearchOk.
        :type: list[int]
        """

        self._agent = agent

    @property
    def alliance(self):
        """
        Gets the alliance of this GetCharactersCharacterIdSearchOk.
        alliance array

        :return: The alliance of this GetCharactersCharacterIdSearchOk.
        :rtype: list[int]
        """
        return self._alliance

    @alliance.setter
    def alliance(self, alliance):
        """
        Sets the alliance of this GetCharactersCharacterIdSearchOk.
        alliance array

        :param alliance: The alliance of this GetCharactersCharacterIdSearchOk.
        :type: list[int]
        """

        self._alliance = alliance

    @property
    def character(self):
        """
        Gets the character of this GetCharactersCharacterIdSearchOk.
        character array

        :return: The character of this GetCharactersCharacterIdSearchOk.
        :rtype: list[int]
        """
        return self._character

    @character.setter
    def character(self, character):
        """
        Sets the character of this GetCharactersCharacterIdSearchOk.
        character array

        :param character: The character of this GetCharactersCharacterIdSearchOk.
        :type: list[int]
        """

        self._character = character

    @property
    def constellation(self):
        """
        Gets the constellation of this GetCharactersCharacterIdSearchOk.
        constellation array

        :return: The constellation of this GetCharactersCharacterIdSearchOk.
        :rtype: list[int]
        """
        return self._constellation

    @constellation.setter
    def constellation(self, constellation):
        """
        Sets the constellation of this GetCharactersCharacterIdSearchOk.
        constellation array

        :param constellation: The constellation of this GetCharactersCharacterIdSearchOk.
        :type: list[int]
        """

        self._constellation = constellation

    @property
    def corporation(self):
        """
        Gets the corporation of this GetCharactersCharacterIdSearchOk.
        corporation array

        :return: The corporation of this GetCharactersCharacterIdSearchOk.
        :rtype: list[int]
        """
        return self._corporation

    @corporation.setter
    def corporation(self, corporation):
        """
        Sets the corporation of this GetCharactersCharacterIdSearchOk.
        corporation array

        :param corporation: The corporation of this GetCharactersCharacterIdSearchOk.
        :type: list[int]
        """

        self._corporation = corporation

    @property
    def faction(self):
        """
        Gets the faction of this GetCharactersCharacterIdSearchOk.
        faction array

        :return: The faction of this GetCharactersCharacterIdSearchOk.
        :rtype: list[int]
        """
        return self._faction

    @faction.setter
    def faction(self, faction):
        """
        Sets the faction of this GetCharactersCharacterIdSearchOk.
        faction array

        :param faction: The faction of this GetCharactersCharacterIdSearchOk.
        :type: list[int]
        """

        self._faction = faction

    @property
    def inventorytype(self):
        """
        Gets the inventorytype of this GetCharactersCharacterIdSearchOk.
        inventorytype array

        :return: The inventorytype of this GetCharactersCharacterIdSearchOk.
        :rtype: list[int]
        """
        return self._inventorytype

    @inventorytype.setter
    def inventorytype(self, inventorytype):
        """
        Sets the inventorytype of this GetCharactersCharacterIdSearchOk.
        inventorytype array

        :param inventorytype: The inventorytype of this GetCharactersCharacterIdSearchOk.
        :type: list[int]
        """

        self._inventorytype = inventorytype

    @property
    def region(self):
        """
        Gets the region of this GetCharactersCharacterIdSearchOk.
        region array

        :return: The region of this GetCharactersCharacterIdSearchOk.
        :rtype: list[int]
        """
        return self._region

    @region.setter
    def region(self, region):
        """
        Sets the region of this GetCharactersCharacterIdSearchOk.
        region array

        :param region: The region of this GetCharactersCharacterIdSearchOk.
        :type: list[int]
        """

        self._region = region

    @property
    def solarsystem(self):
        """
        Gets the solarsystem of this GetCharactersCharacterIdSearchOk.
        solarsystem array

        :return: The solarsystem of this GetCharactersCharacterIdSearchOk.
        :rtype: list[int]
        """
        return self._solarsystem

    @solarsystem.setter
    def solarsystem(self, solarsystem):
        """
        Sets the solarsystem of this GetCharactersCharacterIdSearchOk.
        solarsystem array

        :param solarsystem: The solarsystem of this GetCharactersCharacterIdSearchOk.
        :type: list[int]
        """

        self._solarsystem = solarsystem

    @property
    def station(self):
        """
        Gets the station of this GetCharactersCharacterIdSearchOk.
        station array

        :return: The station of this GetCharactersCharacterIdSearchOk.
        :rtype: list[int]
        """
        return self._station

    @station.setter
    def station(self, station):
        """
        Sets the station of this GetCharactersCharacterIdSearchOk.
        station array

        :param station: The station of this GetCharactersCharacterIdSearchOk.
        :type: list[int]
        """

        self._station = station

    @property
    def structure(self):
        """
        Gets the structure of this GetCharactersCharacterIdSearchOk.
        structure array

        :return: The structure of this GetCharactersCharacterIdSearchOk.
        :rtype: list[int]
        """
        return self._structure

    @structure.setter
    def structure(self, structure):
        """
        Sets the structure of this GetCharactersCharacterIdSearchOk.
        structure array

        :param structure: The structure of this GetCharactersCharacterIdSearchOk.
        :type: list[int]
        """

        self._structure = structure

    @property
    def wormhole(self):
        """
        Gets the wormhole of this GetCharactersCharacterIdSearchOk.
        wormhole array

        :return: The wormhole of this GetCharactersCharacterIdSearchOk.
        :rtype: list[int]
        """
        return self._wormhole

    @wormhole.setter
    def wormhole(self, wormhole):
        """
        Sets the wormhole of this GetCharactersCharacterIdSearchOk.
        wormhole array

        :param wormhole: The wormhole of this GetCharactersCharacterIdSearchOk.
        :type: list[int]
        """

        self._wormhole = wormhole

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
        if not isinstance(other, GetCharactersCharacterIdSearchOk):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
