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


class GetCorporationsCorporationIdAlliancehistoryAlliance(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, alliance_id=None, is_deleted=None):
        """
        GetCorporationsCorporationIdAlliancehistoryAlliance - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'alliance_id': 'int',
            'is_deleted': 'bool'
        }

        self.attribute_map = {
            'alliance_id': 'alliance_id',
            'is_deleted': 'is_deleted'
        }

        self._alliance_id = alliance_id
        self._is_deleted = is_deleted

    @property
    def alliance_id(self):
        """
        Gets the alliance_id of this GetCorporationsCorporationIdAlliancehistoryAlliance.
        alliance_id integer

        :return: The alliance_id of this GetCorporationsCorporationIdAlliancehistoryAlliance.
        :rtype: int
        """
        return self._alliance_id

    @alliance_id.setter
    def alliance_id(self, alliance_id):
        """
        Sets the alliance_id of this GetCorporationsCorporationIdAlliancehistoryAlliance.
        alliance_id integer

        :param alliance_id: The alliance_id of this GetCorporationsCorporationIdAlliancehistoryAlliance.
        :type: int
        """
        if alliance_id is None:
            raise ValueError("Invalid value for `alliance_id`, must not be `None`")

        self._alliance_id = alliance_id

    @property
    def is_deleted(self):
        """
        Gets the is_deleted of this GetCorporationsCorporationIdAlliancehistoryAlliance.
        True if the alliance has been deleted

        :return: The is_deleted of this GetCorporationsCorporationIdAlliancehistoryAlliance.
        :rtype: bool
        """
        return self._is_deleted

    @is_deleted.setter
    def is_deleted(self, is_deleted):
        """
        Sets the is_deleted of this GetCorporationsCorporationIdAlliancehistoryAlliance.
        True if the alliance has been deleted

        :param is_deleted: The is_deleted of this GetCorporationsCorporationIdAlliancehistoryAlliance.
        :type: bool
        """
        if is_deleted is None:
            raise ValueError("Invalid value for `is_deleted`, must not be `None`")

        self._is_deleted = is_deleted

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
        if not isinstance(other, GetCorporationsCorporationIdAlliancehistoryAlliance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
