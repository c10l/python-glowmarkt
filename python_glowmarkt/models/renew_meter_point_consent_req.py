# coding: utf-8

"""
    Glowmarkt User System

    The document enlists and describes the APIs for the User.  # noqa: E501

    OpenAPI spec version: 1.0.5
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class RenewMeterPointConsentReq(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'is_valid_until': 'datetime'
    }

    attribute_map = {
        'is_valid_until': 'isValidUntil'
    }

    def __init__(self, is_valid_until=None):  # noqa: E501
        """RenewMeterPointConsentReq - a model defined in Swagger"""  # noqa: E501
        self._is_valid_until = None
        self.discriminator = None
        if is_valid_until is not None:
            self.is_valid_until = is_valid_until

    @property
    def is_valid_until(self):
        """Gets the is_valid_until of this RenewMeterPointConsentReq.  # noqa: E501


        :return: The is_valid_until of this RenewMeterPointConsentReq.  # noqa: E501
        :rtype: datetime
        """
        return self._is_valid_until

    @is_valid_until.setter
    def is_valid_until(self, is_valid_until):
        """Sets the is_valid_until of this RenewMeterPointConsentReq.


        :param is_valid_until: The is_valid_until of this RenewMeterPointConsentReq.  # noqa: E501
        :type: datetime
        """

        self._is_valid_until = is_valid_until

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(RenewMeterPointConsentReq, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RenewMeterPointConsentReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
