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

class MpxnElem(object):
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
        'mpxn': 'str'
    }

    attribute_map = {
        'mpxn': 'mpxn'
    }

    def __init__(self, mpxn=None):  # noqa: E501
        """MpxnElem - a model defined in Swagger"""  # noqa: E501
        self._mpxn = None
        self.discriminator = None
        if mpxn is not None:
            self.mpxn = mpxn

    @property
    def mpxn(self):
        """Gets the mpxn of this MpxnElem.  # noqa: E501


        :return: The mpxn of this MpxnElem.  # noqa: E501
        :rtype: str
        """
        return self._mpxn

    @mpxn.setter
    def mpxn(self, mpxn):
        """Sets the mpxn of this MpxnElem.


        :param mpxn: The mpxn of this MpxnElem.  # noqa: E501
        :type: str
        """

        self._mpxn = mpxn

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
        if issubclass(MpxnElem, dict):
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
        if not isinstance(other, MpxnElem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
