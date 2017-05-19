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


class GetMarketsPrices200Ok(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, adjusted_price=None, average_price=None, type_id=None):
        """
        GetMarketsPrices200Ok - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'adjusted_price': 'float',
            'average_price': 'float',
            'type_id': 'int'
        }

        self.attribute_map = {
            'adjusted_price': 'adjusted_price',
            'average_price': 'average_price',
            'type_id': 'type_id'
        }

        self._adjusted_price = adjusted_price
        self._average_price = average_price
        self._type_id = type_id

    @property
    def adjusted_price(self):
        """
        Gets the adjusted_price of this GetMarketsPrices200Ok.
        adjusted_price number

        :return: The adjusted_price of this GetMarketsPrices200Ok.
        :rtype: float
        """
        return self._adjusted_price

    @adjusted_price.setter
    def adjusted_price(self, adjusted_price):
        """
        Sets the adjusted_price of this GetMarketsPrices200Ok.
        adjusted_price number

        :param adjusted_price: The adjusted_price of this GetMarketsPrices200Ok.
        :type: float
        """

        self._adjusted_price = adjusted_price

    @property
    def average_price(self):
        """
        Gets the average_price of this GetMarketsPrices200Ok.
        average_price number

        :return: The average_price of this GetMarketsPrices200Ok.
        :rtype: float
        """
        return self._average_price

    @average_price.setter
    def average_price(self, average_price):
        """
        Sets the average_price of this GetMarketsPrices200Ok.
        average_price number

        :param average_price: The average_price of this GetMarketsPrices200Ok.
        :type: float
        """

        self._average_price = average_price

    @property
    def type_id(self):
        """
        Gets the type_id of this GetMarketsPrices200Ok.
        type_id integer

        :return: The type_id of this GetMarketsPrices200Ok.
        :rtype: int
        """
        return self._type_id

    @type_id.setter
    def type_id(self, type_id):
        """
        Sets the type_id of this GetMarketsPrices200Ok.
        type_id integer

        :param type_id: The type_id of this GetMarketsPrices200Ok.
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
        if not isinstance(other, GetMarketsPrices200Ok):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
