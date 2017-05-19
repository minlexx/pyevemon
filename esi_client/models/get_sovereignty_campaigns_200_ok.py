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


class GetSovereigntyCampaigns200Ok(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, attackers_score=None, campaign_id=None, constellation_id=None, defender_id=None, defender_score=None, event_type=None, participants=None, solar_system_id=None, start_time=None, structure_id=None):
        """
        GetSovereigntyCampaigns200Ok - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'attackers_score': 'float',
            'campaign_id': 'int',
            'constellation_id': 'int',
            'defender_id': 'int',
            'defender_score': 'float',
            'event_type': 'str',
            'participants': 'list[GetSovereigntyCampaignsParticipant]',
            'solar_system_id': 'int',
            'start_time': 'datetime',
            'structure_id': 'int'
        }

        self.attribute_map = {
            'attackers_score': 'attackers_score',
            'campaign_id': 'campaign_id',
            'constellation_id': 'constellation_id',
            'defender_id': 'defender_id',
            'defender_score': 'defender_score',
            'event_type': 'event_type',
            'participants': 'participants',
            'solar_system_id': 'solar_system_id',
            'start_time': 'start_time',
            'structure_id': 'structure_id'
        }

        self._attackers_score = attackers_score
        self._campaign_id = campaign_id
        self._constellation_id = constellation_id
        self._defender_id = defender_id
        self._defender_score = defender_score
        self._event_type = event_type
        self._participants = participants
        self._solar_system_id = solar_system_id
        self._start_time = start_time
        self._structure_id = structure_id

    @property
    def attackers_score(self):
        """
        Gets the attackers_score of this GetSovereigntyCampaigns200Ok.
        Score for all attacking parties, only present in Defense Events. 

        :return: The attackers_score of this GetSovereigntyCampaigns200Ok.
        :rtype: float
        """
        return self._attackers_score

    @attackers_score.setter
    def attackers_score(self, attackers_score):
        """
        Sets the attackers_score of this GetSovereigntyCampaigns200Ok.
        Score for all attacking parties, only present in Defense Events. 

        :param attackers_score: The attackers_score of this GetSovereigntyCampaigns200Ok.
        :type: float
        """

        self._attackers_score = attackers_score

    @property
    def campaign_id(self):
        """
        Gets the campaign_id of this GetSovereigntyCampaigns200Ok.
        Unique ID for this campaign.

        :return: The campaign_id of this GetSovereigntyCampaigns200Ok.
        :rtype: int
        """
        return self._campaign_id

    @campaign_id.setter
    def campaign_id(self, campaign_id):
        """
        Sets the campaign_id of this GetSovereigntyCampaigns200Ok.
        Unique ID for this campaign.

        :param campaign_id: The campaign_id of this GetSovereigntyCampaigns200Ok.
        :type: int
        """
        if campaign_id is None:
            raise ValueError("Invalid value for `campaign_id`, must not be `None`")

        self._campaign_id = campaign_id

    @property
    def constellation_id(self):
        """
        Gets the constellation_id of this GetSovereigntyCampaigns200Ok.
        The constellation in which the campaign will take place. 

        :return: The constellation_id of this GetSovereigntyCampaigns200Ok.
        :rtype: int
        """
        return self._constellation_id

    @constellation_id.setter
    def constellation_id(self, constellation_id):
        """
        Sets the constellation_id of this GetSovereigntyCampaigns200Ok.
        The constellation in which the campaign will take place. 

        :param constellation_id: The constellation_id of this GetSovereigntyCampaigns200Ok.
        :type: int
        """
        if constellation_id is None:
            raise ValueError("Invalid value for `constellation_id`, must not be `None`")

        self._constellation_id = constellation_id

    @property
    def defender_id(self):
        """
        Gets the defender_id of this GetSovereigntyCampaigns200Ok.
        Defending alliance, only present in Defense Events 

        :return: The defender_id of this GetSovereigntyCampaigns200Ok.
        :rtype: int
        """
        return self._defender_id

    @defender_id.setter
    def defender_id(self, defender_id):
        """
        Sets the defender_id of this GetSovereigntyCampaigns200Ok.
        Defending alliance, only present in Defense Events 

        :param defender_id: The defender_id of this GetSovereigntyCampaigns200Ok.
        :type: int
        """

        self._defender_id = defender_id

    @property
    def defender_score(self):
        """
        Gets the defender_score of this GetSovereigntyCampaigns200Ok.
        Score for the defending alliance, only present in Defense Events. 

        :return: The defender_score of this GetSovereigntyCampaigns200Ok.
        :rtype: float
        """
        return self._defender_score

    @defender_score.setter
    def defender_score(self, defender_score):
        """
        Sets the defender_score of this GetSovereigntyCampaigns200Ok.
        Score for the defending alliance, only present in Defense Events. 

        :param defender_score: The defender_score of this GetSovereigntyCampaigns200Ok.
        :type: float
        """

        self._defender_score = defender_score

    @property
    def event_type(self):
        """
        Gets the event_type of this GetSovereigntyCampaigns200Ok.
        Type of event this campaign is for. tcu_defense, ihub_defense and station_defense are referred to as \"Defense Events\", station_freeport as \"Freeport Events\". 

        :return: The event_type of this GetSovereigntyCampaigns200Ok.
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """
        Sets the event_type of this GetSovereigntyCampaigns200Ok.
        Type of event this campaign is for. tcu_defense, ihub_defense and station_defense are referred to as \"Defense Events\", station_freeport as \"Freeport Events\". 

        :param event_type: The event_type of this GetSovereigntyCampaigns200Ok.
        :type: str
        """
        allowed_values = ["tcu_defense", "ihub_defense", "station_defense", "station_freeport"]
        if event_type not in allowed_values:
            raise ValueError(
                "Invalid value for `event_type` ({0}), must be one of {1}"
                .format(event_type, allowed_values)
            )

        self._event_type = event_type

    @property
    def participants(self):
        """
        Gets the participants of this GetSovereigntyCampaigns200Ok.
        Alliance participating and their respective scores, only present in Freeport Events. 

        :return: The participants of this GetSovereigntyCampaigns200Ok.
        :rtype: list[GetSovereigntyCampaignsParticipant]
        """
        return self._participants

    @participants.setter
    def participants(self, participants):
        """
        Sets the participants of this GetSovereigntyCampaigns200Ok.
        Alliance participating and their respective scores, only present in Freeport Events. 

        :param participants: The participants of this GetSovereigntyCampaigns200Ok.
        :type: list[GetSovereigntyCampaignsParticipant]
        """

        self._participants = participants

    @property
    def solar_system_id(self):
        """
        Gets the solar_system_id of this GetSovereigntyCampaigns200Ok.
        The solar system the structure is located in. 

        :return: The solar_system_id of this GetSovereigntyCampaigns200Ok.
        :rtype: int
        """
        return self._solar_system_id

    @solar_system_id.setter
    def solar_system_id(self, solar_system_id):
        """
        Sets the solar_system_id of this GetSovereigntyCampaigns200Ok.
        The solar system the structure is located in. 

        :param solar_system_id: The solar_system_id of this GetSovereigntyCampaigns200Ok.
        :type: int
        """
        if solar_system_id is None:
            raise ValueError("Invalid value for `solar_system_id`, must not be `None`")

        self._solar_system_id = solar_system_id

    @property
    def start_time(self):
        """
        Gets the start_time of this GetSovereigntyCampaigns200Ok.
        Time the event is scheduled to start. 

        :return: The start_time of this GetSovereigntyCampaigns200Ok.
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """
        Sets the start_time of this GetSovereigntyCampaigns200Ok.
        Time the event is scheduled to start. 

        :param start_time: The start_time of this GetSovereigntyCampaigns200Ok.
        :type: datetime
        """
        if start_time is None:
            raise ValueError("Invalid value for `start_time`, must not be `None`")

        self._start_time = start_time

    @property
    def structure_id(self):
        """
        Gets the structure_id of this GetSovereigntyCampaigns200Ok.
        The structure item ID that is related to this campaign. 

        :return: The structure_id of this GetSovereigntyCampaigns200Ok.
        :rtype: int
        """
        return self._structure_id

    @structure_id.setter
    def structure_id(self, structure_id):
        """
        Sets the structure_id of this GetSovereigntyCampaigns200Ok.
        The structure item ID that is related to this campaign. 

        :param structure_id: The structure_id of this GetSovereigntyCampaigns200Ok.
        :type: int
        """
        if structure_id is None:
            raise ValueError("Invalid value for `structure_id`, must not be `None`")

        self._structure_id = structure_id

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
        if not isinstance(other, GetSovereigntyCampaigns200Ok):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
