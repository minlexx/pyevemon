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


class GetCharactersCharacterIdSkillqueue200Ok(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, finish_date=None, finished_level=None, level_end_sp=None, level_start_sp=None, queue_position=None, skill_id=None, start_date=None, training_start_sp=None):
        """
        GetCharactersCharacterIdSkillqueue200Ok - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'finish_date': 'datetime',
            'finished_level': 'int',
            'level_end_sp': 'int',
            'level_start_sp': 'int',
            'queue_position': 'int',
            'skill_id': 'int',
            'start_date': 'datetime',
            'training_start_sp': 'int'
        }

        self.attribute_map = {
            'finish_date': 'finish_date',
            'finished_level': 'finished_level',
            'level_end_sp': 'level_end_sp',
            'level_start_sp': 'level_start_sp',
            'queue_position': 'queue_position',
            'skill_id': 'skill_id',
            'start_date': 'start_date',
            'training_start_sp': 'training_start_sp'
        }

        self._finish_date = finish_date
        self._finished_level = finished_level
        self._level_end_sp = level_end_sp
        self._level_start_sp = level_start_sp
        self._queue_position = queue_position
        self._skill_id = skill_id
        self._start_date = start_date
        self._training_start_sp = training_start_sp

    @property
    def finish_date(self):
        """
        Gets the finish_date of this GetCharactersCharacterIdSkillqueue200Ok.
        finish_date string

        :return: The finish_date of this GetCharactersCharacterIdSkillqueue200Ok.
        :rtype: datetime
        """
        return self._finish_date

    @finish_date.setter
    def finish_date(self, finish_date):
        """
        Sets the finish_date of this GetCharactersCharacterIdSkillqueue200Ok.
        finish_date string

        :param finish_date: The finish_date of this GetCharactersCharacterIdSkillqueue200Ok.
        :type: datetime
        """

        self._finish_date = finish_date

    @property
    def finished_level(self):
        """
        Gets the finished_level of this GetCharactersCharacterIdSkillqueue200Ok.
        finished_level integer

        :return: The finished_level of this GetCharactersCharacterIdSkillqueue200Ok.
        :rtype: int
        """
        return self._finished_level

    @finished_level.setter
    def finished_level(self, finished_level):
        """
        Sets the finished_level of this GetCharactersCharacterIdSkillqueue200Ok.
        finished_level integer

        :param finished_level: The finished_level of this GetCharactersCharacterIdSkillqueue200Ok.
        :type: int
        """
        if finished_level is None:
            raise ValueError("Invalid value for `finished_level`, must not be `None`")
        if finished_level is not None and finished_level > 5:
            raise ValueError("Invalid value for `finished_level`, must be a value less than or equal to `5`")
        if finished_level is not None and finished_level < 0:
            raise ValueError("Invalid value for `finished_level`, must be a value greater than or equal to `0`")

        self._finished_level = finished_level

    @property
    def level_end_sp(self):
        """
        Gets the level_end_sp of this GetCharactersCharacterIdSkillqueue200Ok.
        level_end_sp integer

        :return: The level_end_sp of this GetCharactersCharacterIdSkillqueue200Ok.
        :rtype: int
        """
        return self._level_end_sp

    @level_end_sp.setter
    def level_end_sp(self, level_end_sp):
        """
        Sets the level_end_sp of this GetCharactersCharacterIdSkillqueue200Ok.
        level_end_sp integer

        :param level_end_sp: The level_end_sp of this GetCharactersCharacterIdSkillqueue200Ok.
        :type: int
        """

        self._level_end_sp = level_end_sp

    @property
    def level_start_sp(self):
        """
        Gets the level_start_sp of this GetCharactersCharacterIdSkillqueue200Ok.
        Amount of SP that was in the skill when it started training it's current level. Used to calculate % of current level complete.

        :return: The level_start_sp of this GetCharactersCharacterIdSkillqueue200Ok.
        :rtype: int
        """
        return self._level_start_sp

    @level_start_sp.setter
    def level_start_sp(self, level_start_sp):
        """
        Sets the level_start_sp of this GetCharactersCharacterIdSkillqueue200Ok.
        Amount of SP that was in the skill when it started training it's current level. Used to calculate % of current level complete.

        :param level_start_sp: The level_start_sp of this GetCharactersCharacterIdSkillqueue200Ok.
        :type: int
        """

        self._level_start_sp = level_start_sp

    @property
    def queue_position(self):
        """
        Gets the queue_position of this GetCharactersCharacterIdSkillqueue200Ok.
        queue_position integer

        :return: The queue_position of this GetCharactersCharacterIdSkillqueue200Ok.
        :rtype: int
        """
        return self._queue_position

    @queue_position.setter
    def queue_position(self, queue_position):
        """
        Sets the queue_position of this GetCharactersCharacterIdSkillqueue200Ok.
        queue_position integer

        :param queue_position: The queue_position of this GetCharactersCharacterIdSkillqueue200Ok.
        :type: int
        """
        if queue_position is None:
            raise ValueError("Invalid value for `queue_position`, must not be `None`")

        self._queue_position = queue_position

    @property
    def skill_id(self):
        """
        Gets the skill_id of this GetCharactersCharacterIdSkillqueue200Ok.
        skill_id integer

        :return: The skill_id of this GetCharactersCharacterIdSkillqueue200Ok.
        :rtype: int
        """
        return self._skill_id

    @skill_id.setter
    def skill_id(self, skill_id):
        """
        Sets the skill_id of this GetCharactersCharacterIdSkillqueue200Ok.
        skill_id integer

        :param skill_id: The skill_id of this GetCharactersCharacterIdSkillqueue200Ok.
        :type: int
        """
        if skill_id is None:
            raise ValueError("Invalid value for `skill_id`, must not be `None`")

        self._skill_id = skill_id

    @property
    def start_date(self):
        """
        Gets the start_date of this GetCharactersCharacterIdSkillqueue200Ok.
        start_date string

        :return: The start_date of this GetCharactersCharacterIdSkillqueue200Ok.
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """
        Sets the start_date of this GetCharactersCharacterIdSkillqueue200Ok.
        start_date string

        :param start_date: The start_date of this GetCharactersCharacterIdSkillqueue200Ok.
        :type: datetime
        """

        self._start_date = start_date

    @property
    def training_start_sp(self):
        """
        Gets the training_start_sp of this GetCharactersCharacterIdSkillqueue200Ok.
        training_start_sp integer

        :return: The training_start_sp of this GetCharactersCharacterIdSkillqueue200Ok.
        :rtype: int
        """
        return self._training_start_sp

    @training_start_sp.setter
    def training_start_sp(self, training_start_sp):
        """
        Sets the training_start_sp of this GetCharactersCharacterIdSkillqueue200Ok.
        training_start_sp integer

        :param training_start_sp: The training_start_sp of this GetCharactersCharacterIdSkillqueue200Ok.
        :type: int
        """

        self._training_start_sp = training_start_sp

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
        if not isinstance(other, GetCharactersCharacterIdSkillqueue200Ok):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other