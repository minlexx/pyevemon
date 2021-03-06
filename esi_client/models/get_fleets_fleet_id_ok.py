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


class GetFleetsFleetIdOk(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, is_free_move=None, is_registered=None, is_voice_enabled=None, motd=None):
        """
        GetFleetsFleetIdOk - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'is_free_move': 'bool',
            'is_registered': 'bool',
            'is_voice_enabled': 'bool',
            'motd': 'str'
        }

        self.attribute_map = {
            'is_free_move': 'is_free_move',
            'is_registered': 'is_registered',
            'is_voice_enabled': 'is_voice_enabled',
            'motd': 'motd'
        }

        self._is_free_move = is_free_move
        self._is_registered = is_registered
        self._is_voice_enabled = is_voice_enabled
        self._motd = motd

    @property
    def is_free_move(self):
        """
        Gets the is_free_move of this GetFleetsFleetIdOk.
        Is free-move enabled

        :return: The is_free_move of this GetFleetsFleetIdOk.
        :rtype: bool
        """
        return self._is_free_move

    @is_free_move.setter
    def is_free_move(self, is_free_move):
        """
        Sets the is_free_move of this GetFleetsFleetIdOk.
        Is free-move enabled

        :param is_free_move: The is_free_move of this GetFleetsFleetIdOk.
        :type: bool
        """
        if is_free_move is None:
            raise ValueError("Invalid value for `is_free_move`, must not be `None`")

        self._is_free_move = is_free_move

    @property
    def is_registered(self):
        """
        Gets the is_registered of this GetFleetsFleetIdOk.
        Does the fleet have an active fleet advertisement

        :return: The is_registered of this GetFleetsFleetIdOk.
        :rtype: bool
        """
        return self._is_registered

    @is_registered.setter
    def is_registered(self, is_registered):
        """
        Sets the is_registered of this GetFleetsFleetIdOk.
        Does the fleet have an active fleet advertisement

        :param is_registered: The is_registered of this GetFleetsFleetIdOk.
        :type: bool
        """
        if is_registered is None:
            raise ValueError("Invalid value for `is_registered`, must not be `None`")

        self._is_registered = is_registered

    @property
    def is_voice_enabled(self):
        """
        Gets the is_voice_enabled of this GetFleetsFleetIdOk.
        Is EVE Voice enabled

        :return: The is_voice_enabled of this GetFleetsFleetIdOk.
        :rtype: bool
        """
        return self._is_voice_enabled

    @is_voice_enabled.setter
    def is_voice_enabled(self, is_voice_enabled):
        """
        Sets the is_voice_enabled of this GetFleetsFleetIdOk.
        Is EVE Voice enabled

        :param is_voice_enabled: The is_voice_enabled of this GetFleetsFleetIdOk.
        :type: bool
        """
        if is_voice_enabled is None:
            raise ValueError("Invalid value for `is_voice_enabled`, must not be `None`")

        self._is_voice_enabled = is_voice_enabled

    @property
    def motd(self):
        """
        Gets the motd of this GetFleetsFleetIdOk.
        Fleet MOTD in CCP flavoured HTML

        :return: The motd of this GetFleetsFleetIdOk.
        :rtype: str
        """
        return self._motd

    @motd.setter
    def motd(self, motd):
        """
        Sets the motd of this GetFleetsFleetIdOk.
        Fleet MOTD in CCP flavoured HTML

        :param motd: The motd of this GetFleetsFleetIdOk.
        :type: str
        """
        if motd is None:
            raise ValueError("Invalid value for `motd`, must not be `None`")

        self._motd = motd

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
        if not isinstance(other, GetFleetsFleetIdOk):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
