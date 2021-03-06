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


class GetUniverseStationsStationIdOk(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, max_dockable_ship_volume=None, name=None, office_rental_cost=None, owner=None, position=None, race_id=None, reprocessing_efficiency=None, reprocessing_stations_take=None, services=None, station_id=None, system_id=None, type_id=None):
        """
        GetUniverseStationsStationIdOk - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'max_dockable_ship_volume': 'float',
            'name': 'str',
            'office_rental_cost': 'float',
            'owner': 'int',
            'position': 'GetUniverseStationsStationIdPosition',
            'race_id': 'int',
            'reprocessing_efficiency': 'float',
            'reprocessing_stations_take': 'float',
            'services': 'list[str]',
            'station_id': 'int',
            'system_id': 'int',
            'type_id': 'int'
        }

        self.attribute_map = {
            'max_dockable_ship_volume': 'max_dockable_ship_volume',
            'name': 'name',
            'office_rental_cost': 'office_rental_cost',
            'owner': 'owner',
            'position': 'position',
            'race_id': 'race_id',
            'reprocessing_efficiency': 'reprocessing_efficiency',
            'reprocessing_stations_take': 'reprocessing_stations_take',
            'services': 'services',
            'station_id': 'station_id',
            'system_id': 'system_id',
            'type_id': 'type_id'
        }

        self._max_dockable_ship_volume = max_dockable_ship_volume
        self._name = name
        self._office_rental_cost = office_rental_cost
        self._owner = owner
        self._position = position
        self._race_id = race_id
        self._reprocessing_efficiency = reprocessing_efficiency
        self._reprocessing_stations_take = reprocessing_stations_take
        self._services = services
        self._station_id = station_id
        self._system_id = system_id
        self._type_id = type_id

    @property
    def max_dockable_ship_volume(self):
        """
        Gets the max_dockable_ship_volume of this GetUniverseStationsStationIdOk.
        max_dockable_ship_volume number

        :return: The max_dockable_ship_volume of this GetUniverseStationsStationIdOk.
        :rtype: float
        """
        return self._max_dockable_ship_volume

    @max_dockable_ship_volume.setter
    def max_dockable_ship_volume(self, max_dockable_ship_volume):
        """
        Sets the max_dockable_ship_volume of this GetUniverseStationsStationIdOk.
        max_dockable_ship_volume number

        :param max_dockable_ship_volume: The max_dockable_ship_volume of this GetUniverseStationsStationIdOk.
        :type: float
        """
        if max_dockable_ship_volume is None:
            raise ValueError("Invalid value for `max_dockable_ship_volume`, must not be `None`")

        self._max_dockable_ship_volume = max_dockable_ship_volume

    @property
    def name(self):
        """
        Gets the name of this GetUniverseStationsStationIdOk.
        name string

        :return: The name of this GetUniverseStationsStationIdOk.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this GetUniverseStationsStationIdOk.
        name string

        :param name: The name of this GetUniverseStationsStationIdOk.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def office_rental_cost(self):
        """
        Gets the office_rental_cost of this GetUniverseStationsStationIdOk.
        office_rental_cost number

        :return: The office_rental_cost of this GetUniverseStationsStationIdOk.
        :rtype: float
        """
        return self._office_rental_cost

    @office_rental_cost.setter
    def office_rental_cost(self, office_rental_cost):
        """
        Sets the office_rental_cost of this GetUniverseStationsStationIdOk.
        office_rental_cost number

        :param office_rental_cost: The office_rental_cost of this GetUniverseStationsStationIdOk.
        :type: float
        """
        if office_rental_cost is None:
            raise ValueError("Invalid value for `office_rental_cost`, must not be `None`")

        self._office_rental_cost = office_rental_cost

    @property
    def owner(self):
        """
        Gets the owner of this GetUniverseStationsStationIdOk.
        ID of the corporation that controls this station

        :return: The owner of this GetUniverseStationsStationIdOk.
        :rtype: int
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """
        Sets the owner of this GetUniverseStationsStationIdOk.
        ID of the corporation that controls this station

        :param owner: The owner of this GetUniverseStationsStationIdOk.
        :type: int
        """

        self._owner = owner

    @property
    def position(self):
        """
        Gets the position of this GetUniverseStationsStationIdOk.

        :return: The position of this GetUniverseStationsStationIdOk.
        :rtype: GetUniverseStationsStationIdPosition
        """
        return self._position

    @position.setter
    def position(self, position):
        """
        Sets the position of this GetUniverseStationsStationIdOk.

        :param position: The position of this GetUniverseStationsStationIdOk.
        :type: GetUniverseStationsStationIdPosition
        """

        self._position = position

    @property
    def race_id(self):
        """
        Gets the race_id of this GetUniverseStationsStationIdOk.
        race_id integer

        :return: The race_id of this GetUniverseStationsStationIdOk.
        :rtype: int
        """
        return self._race_id

    @race_id.setter
    def race_id(self, race_id):
        """
        Sets the race_id of this GetUniverseStationsStationIdOk.
        race_id integer

        :param race_id: The race_id of this GetUniverseStationsStationIdOk.
        :type: int
        """

        self._race_id = race_id

    @property
    def reprocessing_efficiency(self):
        """
        Gets the reprocessing_efficiency of this GetUniverseStationsStationIdOk.
        reprocessing_efficiency number

        :return: The reprocessing_efficiency of this GetUniverseStationsStationIdOk.
        :rtype: float
        """
        return self._reprocessing_efficiency

    @reprocessing_efficiency.setter
    def reprocessing_efficiency(self, reprocessing_efficiency):
        """
        Sets the reprocessing_efficiency of this GetUniverseStationsStationIdOk.
        reprocessing_efficiency number

        :param reprocessing_efficiency: The reprocessing_efficiency of this GetUniverseStationsStationIdOk.
        :type: float
        """
        if reprocessing_efficiency is None:
            raise ValueError("Invalid value for `reprocessing_efficiency`, must not be `None`")

        self._reprocessing_efficiency = reprocessing_efficiency

    @property
    def reprocessing_stations_take(self):
        """
        Gets the reprocessing_stations_take of this GetUniverseStationsStationIdOk.
        reprocessing_stations_take number

        :return: The reprocessing_stations_take of this GetUniverseStationsStationIdOk.
        :rtype: float
        """
        return self._reprocessing_stations_take

    @reprocessing_stations_take.setter
    def reprocessing_stations_take(self, reprocessing_stations_take):
        """
        Sets the reprocessing_stations_take of this GetUniverseStationsStationIdOk.
        reprocessing_stations_take number

        :param reprocessing_stations_take: The reprocessing_stations_take of this GetUniverseStationsStationIdOk.
        :type: float
        """
        if reprocessing_stations_take is None:
            raise ValueError("Invalid value for `reprocessing_stations_take`, must not be `None`")

        self._reprocessing_stations_take = reprocessing_stations_take

    @property
    def services(self):
        """
        Gets the services of this GetUniverseStationsStationIdOk.
        services array

        :return: The services of this GetUniverseStationsStationIdOk.
        :rtype: list[str]
        """
        return self._services

    @services.setter
    def services(self, services):
        """
        Sets the services of this GetUniverseStationsStationIdOk.
        services array

        :param services: The services of this GetUniverseStationsStationIdOk.
        :type: list[str]
        """
        allowed_values = ["bounty-missions", "assasination-missions", "courier-missions", "interbus", "reprocessing-plant", "refinery", "market", "black-market", "stock-exchange", "cloning", "surgery", "dna-therapy", "repair-facilities", "factory", "labratory", "gambling", "fitting", "paintshop", "news", "storage", "insurance", "docking", "office-rental", "jump-clone-facility", "loyalty-point-store", "navy-offices", "security-offices"]
        if not set(services).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `services` [{0}], must be a subset of [{1}]"
                .format(", ".join(map(str, set(services)-set(allowed_values))),
                        ", ".join(map(str, allowed_values)))
            )

        self._services = services

    @property
    def station_id(self):
        """
        Gets the station_id of this GetUniverseStationsStationIdOk.
        station_id integer

        :return: The station_id of this GetUniverseStationsStationIdOk.
        :rtype: int
        """
        return self._station_id

    @station_id.setter
    def station_id(self, station_id):
        """
        Sets the station_id of this GetUniverseStationsStationIdOk.
        station_id integer

        :param station_id: The station_id of this GetUniverseStationsStationIdOk.
        :type: int
        """
        if station_id is None:
            raise ValueError("Invalid value for `station_id`, must not be `None`")

        self._station_id = station_id

    @property
    def system_id(self):
        """
        Gets the system_id of this GetUniverseStationsStationIdOk.
        The solar system this station is in

        :return: The system_id of this GetUniverseStationsStationIdOk.
        :rtype: int
        """
        return self._system_id

    @system_id.setter
    def system_id(self, system_id):
        """
        Sets the system_id of this GetUniverseStationsStationIdOk.
        The solar system this station is in

        :param system_id: The system_id of this GetUniverseStationsStationIdOk.
        :type: int
        """
        if system_id is None:
            raise ValueError("Invalid value for `system_id`, must not be `None`")

        self._system_id = system_id

    @property
    def type_id(self):
        """
        Gets the type_id of this GetUniverseStationsStationIdOk.
        type_id integer

        :return: The type_id of this GetUniverseStationsStationIdOk.
        :rtype: int
        """
        return self._type_id

    @type_id.setter
    def type_id(self, type_id):
        """
        Sets the type_id of this GetUniverseStationsStationIdOk.
        type_id integer

        :param type_id: The type_id of this GetUniverseStationsStationIdOk.
        :type: int
        """
        if type_id is None:
            raise ValueError("Invalid value for `type_id`, must not be `None`")

        self._type_id = type_id

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
        if not isinstance(other, GetUniverseStationsStationIdOk):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
