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


class GetWarsWarIdDefender(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, alliance_id=None, corporation_id=None, isk_destroyed=None, ships_killed=None):
        """
        GetWarsWarIdDefender - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'alliance_id': 'int',
            'corporation_id': 'int',
            'isk_destroyed': 'float',
            'ships_killed': 'int'
        }

        self.attribute_map = {
            'alliance_id': 'alliance_id',
            'corporation_id': 'corporation_id',
            'isk_destroyed': 'isk_destroyed',
            'ships_killed': 'ships_killed'
        }

        self._alliance_id = alliance_id
        self._corporation_id = corporation_id
        self._isk_destroyed = isk_destroyed
        self._ships_killed = ships_killed

    @property
    def alliance_id(self):
        """
        Gets the alliance_id of this GetWarsWarIdDefender.
        Alliance ID if and only if the defender is an alliance

        :return: The alliance_id of this GetWarsWarIdDefender.
        :rtype: int
        """
        return self._alliance_id

    @alliance_id.setter
    def alliance_id(self, alliance_id):
        """
        Sets the alliance_id of this GetWarsWarIdDefender.
        Alliance ID if and only if the defender is an alliance

        :param alliance_id: The alliance_id of this GetWarsWarIdDefender.
        :type: int
        """

        self._alliance_id = alliance_id

    @property
    def corporation_id(self):
        """
        Gets the corporation_id of this GetWarsWarIdDefender.
        Corporation ID if and only if the defender is a corporation

        :return: The corporation_id of this GetWarsWarIdDefender.
        :rtype: int
        """
        return self._corporation_id

    @corporation_id.setter
    def corporation_id(self, corporation_id):
        """
        Sets the corporation_id of this GetWarsWarIdDefender.
        Corporation ID if and only if the defender is a corporation

        :param corporation_id: The corporation_id of this GetWarsWarIdDefender.
        :type: int
        """

        self._corporation_id = corporation_id

    @property
    def isk_destroyed(self):
        """
        Gets the isk_destroyed of this GetWarsWarIdDefender.
        ISK value of ships the defender has killed

        :return: The isk_destroyed of this GetWarsWarIdDefender.
        :rtype: float
        """
        return self._isk_destroyed

    @isk_destroyed.setter
    def isk_destroyed(self, isk_destroyed):
        """
        Sets the isk_destroyed of this GetWarsWarIdDefender.
        ISK value of ships the defender has killed

        :param isk_destroyed: The isk_destroyed of this GetWarsWarIdDefender.
        :type: float
        """
        if isk_destroyed is None:
            raise ValueError("Invalid value for `isk_destroyed`, must not be `None`")

        self._isk_destroyed = isk_destroyed

    @property
    def ships_killed(self):
        """
        Gets the ships_killed of this GetWarsWarIdDefender.
        The number of ships the defender has killed

        :return: The ships_killed of this GetWarsWarIdDefender.
        :rtype: int
        """
        return self._ships_killed

    @ships_killed.setter
    def ships_killed(self, ships_killed):
        """
        Sets the ships_killed of this GetWarsWarIdDefender.
        The number of ships the defender has killed

        :param ships_killed: The ships_killed of this GetWarsWarIdDefender.
        :type: int
        """
        if ships_killed is None:
            raise ValueError("Invalid value for `ships_killed`, must not be `None`")

        self._ships_killed = ships_killed

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
        if not isinstance(other, GetWarsWarIdDefender):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other