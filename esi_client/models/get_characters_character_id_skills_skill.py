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


class GetCharactersCharacterIdSkillsSkill(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, current_skill_level=None, skill_id=None, skillpoints_in_skill=None):
        """
        GetCharactersCharacterIdSkillsSkill - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'current_skill_level': 'int',
            'skill_id': 'int',
            'skillpoints_in_skill': 'int'
        }

        self.attribute_map = {
            'current_skill_level': 'current_skill_level',
            'skill_id': 'skill_id',
            'skillpoints_in_skill': 'skillpoints_in_skill'
        }

        self._current_skill_level = current_skill_level
        self._skill_id = skill_id
        self._skillpoints_in_skill = skillpoints_in_skill

    @property
    def current_skill_level(self):
        """
        Gets the current_skill_level of this GetCharactersCharacterIdSkillsSkill.
        current_skill_level integer

        :return: The current_skill_level of this GetCharactersCharacterIdSkillsSkill.
        :rtype: int
        """
        return self._current_skill_level

    @current_skill_level.setter
    def current_skill_level(self, current_skill_level):
        """
        Sets the current_skill_level of this GetCharactersCharacterIdSkillsSkill.
        current_skill_level integer

        :param current_skill_level: The current_skill_level of this GetCharactersCharacterIdSkillsSkill.
        :type: int
        """

        self._current_skill_level = current_skill_level

    @property
    def skill_id(self):
        """
        Gets the skill_id of this GetCharactersCharacterIdSkillsSkill.
        skill_id integer

        :return: The skill_id of this GetCharactersCharacterIdSkillsSkill.
        :rtype: int
        """
        return self._skill_id

    @skill_id.setter
    def skill_id(self, skill_id):
        """
        Sets the skill_id of this GetCharactersCharacterIdSkillsSkill.
        skill_id integer

        :param skill_id: The skill_id of this GetCharactersCharacterIdSkillsSkill.
        :type: int
        """

        self._skill_id = skill_id

    @property
    def skillpoints_in_skill(self):
        """
        Gets the skillpoints_in_skill of this GetCharactersCharacterIdSkillsSkill.
        skillpoints_in_skill integer

        :return: The skillpoints_in_skill of this GetCharactersCharacterIdSkillsSkill.
        :rtype: int
        """
        return self._skillpoints_in_skill

    @skillpoints_in_skill.setter
    def skillpoints_in_skill(self, skillpoints_in_skill):
        """
        Sets the skillpoints_in_skill of this GetCharactersCharacterIdSkillsSkill.
        skillpoints_in_skill integer

        :param skillpoints_in_skill: The skillpoints_in_skill of this GetCharactersCharacterIdSkillsSkill.
        :type: int
        """

        self._skillpoints_in_skill = skillpoints_in_skill

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
        if not isinstance(other, GetCharactersCharacterIdSkillsSkill):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
