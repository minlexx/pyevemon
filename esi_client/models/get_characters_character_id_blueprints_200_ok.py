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


class GetCharactersCharacterIdBlueprints200Ok(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, item_id=None, location_flag=None, location_id=None, material_efficiency=None, quantity=None, runs=None, time_efficiency=None, type_id=None):
        """
        GetCharactersCharacterIdBlueprints200Ok - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'item_id': 'int',
            'location_flag': 'str',
            'location_id': 'int',
            'material_efficiency': 'int',
            'quantity': 'int',
            'runs': 'int',
            'time_efficiency': 'int',
            'type_id': 'int'
        }

        self.attribute_map = {
            'item_id': 'item_id',
            'location_flag': 'location_flag',
            'location_id': 'location_id',
            'material_efficiency': 'material_efficiency',
            'quantity': 'quantity',
            'runs': 'runs',
            'time_efficiency': 'time_efficiency',
            'type_id': 'type_id'
        }

        self._item_id = item_id
        self._location_flag = location_flag
        self._location_id = location_id
        self._material_efficiency = material_efficiency
        self._quantity = quantity
        self._runs = runs
        self._time_efficiency = time_efficiency
        self._type_id = type_id

    @property
    def item_id(self):
        """
        Gets the item_id of this GetCharactersCharacterIdBlueprints200Ok.
        Unique ID for this item. The ID of an item is stable if that item is not repackaged, stacked, detached from a stack, assembled, or otherwise altered. If an item is changed in one of these ways, then the ID will also change (see notes below).

        :return: The item_id of this GetCharactersCharacterIdBlueprints200Ok.
        :rtype: int
        """
        return self._item_id

    @item_id.setter
    def item_id(self, item_id):
        """
        Sets the item_id of this GetCharactersCharacterIdBlueprints200Ok.
        Unique ID for this item. The ID of an item is stable if that item is not repackaged, stacked, detached from a stack, assembled, or otherwise altered. If an item is changed in one of these ways, then the ID will also change (see notes below).

        :param item_id: The item_id of this GetCharactersCharacterIdBlueprints200Ok.
        :type: int
        """
        if item_id is None:
            raise ValueError("Invalid value for `item_id`, must not be `None`")

        self._item_id = item_id

    @property
    def location_flag(self):
        """
        Gets the location_flag of this GetCharactersCharacterIdBlueprints200Ok.
        Indicates something about this item's storage location. The flag is used to differentiate between hangar divisions, drone bay, fitting location, and similar.

        :return: The location_flag of this GetCharactersCharacterIdBlueprints200Ok.
        :rtype: str
        """
        return self._location_flag

    @location_flag.setter
    def location_flag(self, location_flag):
        """
        Sets the location_flag of this GetCharactersCharacterIdBlueprints200Ok.
        Indicates something about this item's storage location. The flag is used to differentiate between hangar divisions, drone bay, fitting location, and similar.

        :param location_flag: The location_flag of this GetCharactersCharacterIdBlueprints200Ok.
        :type: str
        """
        allowed_values = ["AutoFit", "Cargo", "CorpseBay", "DroneBay", "FleetHangar", "Deliveries", "HiddenModifiers", "Hangar", "HangarAll", "LoSlot0", "LoSlot1", "LoSlot2", "LoSlot3", "LoSlot4", "LoSlot5", "LoSlot6", "LoSlot7", "MedSlot0", "MedSlot1", "MedSlot2", "MedSlot3", "MedSlot4", "MedSlot5", "MedSlot6", "MedSlot7", "HiSlot0", "HiSlot1", "HiSlot2", "HiSlot3", "HiSlot4", "HiSlot5", "HiSlot6", "HiSlot7", "AssetSafety", "Locked", "Unlocked", "Implant", "QuafeBay", "RigSlot0", "RigSlot1", "RigSlot2", "RigSlot3", "RigSlot4", "RigSlot5", "RigSlot6", "RigSlot7", "ShipHangar", "SpecializedFuelBay", "SpecializedOreHold", "SpecializedGasHold", "SpecializedMineralHold", "SpecializedSalvageHold", "SpecializedShipHold", "SpecializedSmallShipHold", "SpecializedMediumShipHold", "SpecializedLargeShipHold", "SpecializedIndustrialShipHold", "SpecializedAmmoHold", "SpecializedCommandCenterHold", "SpecializedPlanetaryCommoditiesHold", "SpecializedMaterialBay", "SubSystemSlot0", "SubSystemSlot1", "SubSystemSlot2", "SubSystemSlot3", "SubSystemSlot4", "SubSystemSlot5", "SubSystemSlot6", "SubSystemSlot7", "FighterBay", "FighterTube0", "FighterTube1", "FighterTube2", "FighterTube3", "FighterTube4", "Module"]
        if location_flag not in allowed_values:
            raise ValueError(
                "Invalid value for `location_flag` ({0}), must be one of {1}"
                .format(location_flag, allowed_values)
            )

        self._location_flag = location_flag

    @property
    def location_id(self):
        """
        Gets the location_id of this GetCharactersCharacterIdBlueprints200Ok.
        References a solar system, station or itemID if this blueprint is located within a container. If an itemID the Character - AssetList API must be queried to find the container using the itemID, from which the correct location of the Blueprint can be derived.

        :return: The location_id of this GetCharactersCharacterIdBlueprints200Ok.
        :rtype: int
        """
        return self._location_id

    @location_id.setter
    def location_id(self, location_id):
        """
        Sets the location_id of this GetCharactersCharacterIdBlueprints200Ok.
        References a solar system, station or itemID if this blueprint is located within a container. If an itemID the Character - AssetList API must be queried to find the container using the itemID, from which the correct location of the Blueprint can be derived.

        :param location_id: The location_id of this GetCharactersCharacterIdBlueprints200Ok.
        :type: int
        """
        if location_id is None:
            raise ValueError("Invalid value for `location_id`, must not be `None`")

        self._location_id = location_id

    @property
    def material_efficiency(self):
        """
        Gets the material_efficiency of this GetCharactersCharacterIdBlueprints200Ok.
        Material Efficiency Level of the blueprint, can be any integer between 0 and 10.

        :return: The material_efficiency of this GetCharactersCharacterIdBlueprints200Ok.
        :rtype: int
        """
        return self._material_efficiency

    @material_efficiency.setter
    def material_efficiency(self, material_efficiency):
        """
        Sets the material_efficiency of this GetCharactersCharacterIdBlueprints200Ok.
        Material Efficiency Level of the blueprint, can be any integer between 0 and 10.

        :param material_efficiency: The material_efficiency of this GetCharactersCharacterIdBlueprints200Ok.
        :type: int
        """
        if material_efficiency is None:
            raise ValueError("Invalid value for `material_efficiency`, must not be `None`")

        self._material_efficiency = material_efficiency

    @property
    def quantity(self):
        """
        Gets the quantity of this GetCharactersCharacterIdBlueprints200Ok.
        Typically will be -1 or -2 designating a singleton item, where -1 is an original and -2 is a copy. It can be a positive integer if it is a stack of blueprint originals fresh from the market (no activities performed on them yet).

        :return: The quantity of this GetCharactersCharacterIdBlueprints200Ok.
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """
        Sets the quantity of this GetCharactersCharacterIdBlueprints200Ok.
        Typically will be -1 or -2 designating a singleton item, where -1 is an original and -2 is a copy. It can be a positive integer if it is a stack of blueprint originals fresh from the market (no activities performed on them yet).

        :param quantity: The quantity of this GetCharactersCharacterIdBlueprints200Ok.
        :type: int
        """
        if quantity is None:
            raise ValueError("Invalid value for `quantity`, must not be `None`")

        self._quantity = quantity

    @property
    def runs(self):
        """
        Gets the runs of this GetCharactersCharacterIdBlueprints200Ok.
        Number of runs remaining if the blueprint is a copy, -1 if it is an original.

        :return: The runs of this GetCharactersCharacterIdBlueprints200Ok.
        :rtype: int
        """
        return self._runs

    @runs.setter
    def runs(self, runs):
        """
        Sets the runs of this GetCharactersCharacterIdBlueprints200Ok.
        Number of runs remaining if the blueprint is a copy, -1 if it is an original.

        :param runs: The runs of this GetCharactersCharacterIdBlueprints200Ok.
        :type: int
        """
        if runs is None:
            raise ValueError("Invalid value for `runs`, must not be `None`")

        self._runs = runs

    @property
    def time_efficiency(self):
        """
        Gets the time_efficiency of this GetCharactersCharacterIdBlueprints200Ok.
        Time Efficiency Level of the blueprint, can be any even integer between 0 and 20.

        :return: The time_efficiency of this GetCharactersCharacterIdBlueprints200Ok.
        :rtype: int
        """
        return self._time_efficiency

    @time_efficiency.setter
    def time_efficiency(self, time_efficiency):
        """
        Sets the time_efficiency of this GetCharactersCharacterIdBlueprints200Ok.
        Time Efficiency Level of the blueprint, can be any even integer between 0 and 20.

        :param time_efficiency: The time_efficiency of this GetCharactersCharacterIdBlueprints200Ok.
        :type: int
        """
        if time_efficiency is None:
            raise ValueError("Invalid value for `time_efficiency`, must not be `None`")

        self._time_efficiency = time_efficiency

    @property
    def type_id(self):
        """
        Gets the type_id of this GetCharactersCharacterIdBlueprints200Ok.
        type_id integer

        :return: The type_id of this GetCharactersCharacterIdBlueprints200Ok.
        :rtype: int
        """
        return self._type_id

    @type_id.setter
    def type_id(self, type_id):
        """
        Sets the type_id of this GetCharactersCharacterIdBlueprints200Ok.
        type_id integer

        :param type_id: The type_id of this GetCharactersCharacterIdBlueprints200Ok.
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
        if not isinstance(other, GetCharactersCharacterIdBlueprints200Ok):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other