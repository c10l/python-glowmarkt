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

class OAuthCodeRes(object):
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
        'account_id': 'str',
        'code': 'str',
        'exp': 'float',
        'name': 'str',
        'valid': 'bool'
    }

    attribute_map = {
        'account_id': 'accountId',
        'code': 'code',
        'exp': 'exp',
        'name': 'name',
        'valid': 'valid'
    }

    def __init__(self, account_id=None, code=None, exp=None, name=None, valid=None):  # noqa: E501
        """OAuthCodeRes - a model defined in Swagger"""  # noqa: E501
        self._account_id = None
        self._code = None
        self._exp = None
        self._name = None
        self._valid = None
        self.discriminator = None
        if account_id is not None:
            self.account_id = account_id
        if code is not None:
            self.code = code
        if exp is not None:
            self.exp = exp
        if name is not None:
            self.name = name
        if valid is not None:
            self.valid = valid

    @property
    def account_id(self):
        """Gets the account_id of this OAuthCodeRes.  # noqa: E501


        :return: The account_id of this OAuthCodeRes.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this OAuthCodeRes.


        :param account_id: The account_id of this OAuthCodeRes.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def code(self):
        """Gets the code of this OAuthCodeRes.  # noqa: E501


        :return: The code of this OAuthCodeRes.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this OAuthCodeRes.


        :param code: The code of this OAuthCodeRes.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def exp(self):
        """Gets the exp of this OAuthCodeRes.  # noqa: E501


        :return: The exp of this OAuthCodeRes.  # noqa: E501
        :rtype: float
        """
        return self._exp

    @exp.setter
    def exp(self, exp):
        """Sets the exp of this OAuthCodeRes.


        :param exp: The exp of this OAuthCodeRes.  # noqa: E501
        :type: float
        """

        self._exp = exp

    @property
    def name(self):
        """Gets the name of this OAuthCodeRes.  # noqa: E501


        :return: The name of this OAuthCodeRes.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OAuthCodeRes.


        :param name: The name of this OAuthCodeRes.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def valid(self):
        """Gets the valid of this OAuthCodeRes.  # noqa: E501


        :return: The valid of this OAuthCodeRes.  # noqa: E501
        :rtype: bool
        """
        return self._valid

    @valid.setter
    def valid(self, valid):
        """Sets the valid of this OAuthCodeRes.


        :param valid: The valid of this OAuthCodeRes.  # noqa: E501
        :type: bool
        """

        self._valid = valid

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
        if issubclass(OAuthCodeRes, dict):
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
        if not isinstance(other, OAuthCodeRes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
