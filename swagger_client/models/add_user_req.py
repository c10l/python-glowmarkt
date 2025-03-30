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

class AddUserReq(object):
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
        'application_id': 'str',
        'directory_id': 'str',
        'email': 'str',
        'name': 'str',
        'password': 'str',
        'username': 'str'
    }

    attribute_map = {
        'application_id': 'applicationId',
        'directory_id': 'directoryId',
        'email': 'email',
        'name': 'name',
        'password': 'password',
        'username': 'username'
    }

    def __init__(self, application_id=None, directory_id=None, email=None, name=None, password=None, username=None):  # noqa: E501
        """AddUserReq - a model defined in Swagger"""  # noqa: E501
        self._application_id = None
        self._directory_id = None
        self._email = None
        self._name = None
        self._password = None
        self._username = None
        self.discriminator = None
        self.application_id = application_id
        self.directory_id = directory_id
        self.email = email
        self.name = name
        self.password = password
        self.username = username

    @property
    def application_id(self):
        """Gets the application_id of this AddUserReq.  # noqa: E501


        :return: The application_id of this AddUserReq.  # noqa: E501
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        """Sets the application_id of this AddUserReq.


        :param application_id: The application_id of this AddUserReq.  # noqa: E501
        :type: str
        """
        if application_id is None:
            raise ValueError("Invalid value for `application_id`, must not be `None`")  # noqa: E501

        self._application_id = application_id

    @property
    def directory_id(self):
        """Gets the directory_id of this AddUserReq.  # noqa: E501


        :return: The directory_id of this AddUserReq.  # noqa: E501
        :rtype: str
        """
        return self._directory_id

    @directory_id.setter
    def directory_id(self, directory_id):
        """Sets the directory_id of this AddUserReq.


        :param directory_id: The directory_id of this AddUserReq.  # noqa: E501
        :type: str
        """
        if directory_id is None:
            raise ValueError("Invalid value for `directory_id`, must not be `None`")  # noqa: E501

        self._directory_id = directory_id

    @property
    def email(self):
        """Gets the email of this AddUserReq.  # noqa: E501


        :return: The email of this AddUserReq.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this AddUserReq.


        :param email: The email of this AddUserReq.  # noqa: E501
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def name(self):
        """Gets the name of this AddUserReq.  # noqa: E501


        :return: The name of this AddUserReq.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AddUserReq.


        :param name: The name of this AddUserReq.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def password(self):
        """Gets the password of this AddUserReq.  # noqa: E501


        :return: The password of this AddUserReq.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this AddUserReq.


        :param password: The password of this AddUserReq.  # noqa: E501
        :type: str
        """
        if password is None:
            raise ValueError("Invalid value for `password`, must not be `None`")  # noqa: E501

        self._password = password

    @property
    def username(self):
        """Gets the username of this AddUserReq.  # noqa: E501


        :return: The username of this AddUserReq.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this AddUserReq.


        :param username: The username of this AddUserReq.  # noqa: E501
        :type: str
        """
        if username is None:
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501

        self._username = username

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
        if issubclass(AddUserReq, dict):
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
        if not isinstance(other, AddUserReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
