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

class UserMeterPointConsentAndVerification(object):
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
        'meter_point_verification': 'list[MeterPointConsentAndVerification]'
    }

    attribute_map = {
        'meter_point_verification': 'meterPointVerification'
    }

    def __init__(self, meter_point_verification=None):  # noqa: E501
        """UserMeterPointConsentAndVerification - a model defined in Swagger"""  # noqa: E501
        self._meter_point_verification = None
        self.discriminator = None
        if meter_point_verification is not None:
            self.meter_point_verification = meter_point_verification

    @property
    def meter_point_verification(self):
        """Gets the meter_point_verification of this UserMeterPointConsentAndVerification.  # noqa: E501


        :return: The meter_point_verification of this UserMeterPointConsentAndVerification.  # noqa: E501
        :rtype: list[MeterPointConsentAndVerification]
        """
        return self._meter_point_verification

    @meter_point_verification.setter
    def meter_point_verification(self, meter_point_verification):
        """Sets the meter_point_verification of this UserMeterPointConsentAndVerification.


        :param meter_point_verification: The meter_point_verification of this UserMeterPointConsentAndVerification.  # noqa: E501
        :type: list[MeterPointConsentAndVerification]
        """

        self._meter_point_verification = meter_point_verification

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
        if issubclass(UserMeterPointConsentAndVerification, dict):
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
        if not isinstance(other, UserMeterPointConsentAndVerification):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
