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


class GetCharactersCharacterIdSkillsOk(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, skills=None, total_sp=None):
        """
        GetCharactersCharacterIdSkillsOk - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'skills': 'list[GetCharactersCharacterIdSkillsSkill]',
            'total_sp': 'int'
        }

        self.attribute_map = {
            'skills': 'skills',
            'total_sp': 'total_sp'
        }

        self._skills = skills
        self._total_sp = total_sp

    @property
    def skills(self):
        """
        Gets the skills of this GetCharactersCharacterIdSkillsOk.
        skills array

        :return: The skills of this GetCharactersCharacterIdSkillsOk.
        :rtype: list[GetCharactersCharacterIdSkillsSkill]
        """
        return self._skills

    @skills.setter
    def skills(self, skills):
        """
        Sets the skills of this GetCharactersCharacterIdSkillsOk.
        skills array

        :param skills: The skills of this GetCharactersCharacterIdSkillsOk.
        :type: list[GetCharactersCharacterIdSkillsSkill]
        """

        self._skills = skills

    @property
    def total_sp(self):
        """
        Gets the total_sp of this GetCharactersCharacterIdSkillsOk.
        total_sp integer

        :return: The total_sp of this GetCharactersCharacterIdSkillsOk.
        :rtype: int
        """
        return self._total_sp

    @total_sp.setter
    def total_sp(self, total_sp):
        """
        Sets the total_sp of this GetCharactersCharacterIdSkillsOk.
        total_sp integer

        :param total_sp: The total_sp of this GetCharactersCharacterIdSkillsOk.
        :type: int
        """

        self._total_sp = total_sp

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
        if not isinstance(other, GetCharactersCharacterIdSkillsOk):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
