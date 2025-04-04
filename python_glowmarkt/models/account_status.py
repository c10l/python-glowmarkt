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

class AccountStatus(object):
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
        'active': 'bool',
        'application_id': 'str',
        'created_at': 'datetime',
        'directory': 'AccountStatusDirectory',
        'directory_id': 'str',
        'status': 'str',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'account_id': 'accountId',
        'active': 'active',
        'application_id': 'applicationId',
        'created_at': 'createdAt',
        'directory': 'directory',
        'directory_id': 'directoryId',
        'status': 'status',
        'updated_at': 'updatedAt'
    }

    def __init__(self, account_id=None, active=None, application_id=None, created_at=None, directory=None, directory_id=None, status=None, updated_at=None):  # noqa: E501
        """AccountStatus - a model defined in Swagger"""  # noqa: E501
        self._account_id = None
        self._active = None
        self._application_id = None
        self._created_at = None
        self._directory = None
        self._directory_id = None
        self._status = None
        self._updated_at = None
        self.discriminator = None
        if account_id is not None:
            self.account_id = account_id
        if active is not None:
            self.active = active
        if application_id is not None:
            self.application_id = application_id
        if created_at is not None:
            self.created_at = created_at
        if directory is not None:
            self.directory = directory
        if directory_id is not None:
            self.directory_id = directory_id
        if status is not None:
            self.status = status
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def account_id(self):
        """Gets the account_id of this AccountStatus.  # noqa: E501


        :return: The account_id of this AccountStatus.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this AccountStatus.


        :param account_id: The account_id of this AccountStatus.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def active(self):
        """Gets the active of this AccountStatus.  # noqa: E501


        :return: The active of this AccountStatus.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this AccountStatus.


        :param active: The active of this AccountStatus.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def application_id(self):
        """Gets the application_id of this AccountStatus.  # noqa: E501


        :return: The application_id of this AccountStatus.  # noqa: E501
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        """Sets the application_id of this AccountStatus.


        :param application_id: The application_id of this AccountStatus.  # noqa: E501
        :type: str
        """

        self._application_id = application_id

    @property
    def created_at(self):
        """Gets the created_at of this AccountStatus.  # noqa: E501


        :return: The created_at of this AccountStatus.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this AccountStatus.


        :param created_at: The created_at of this AccountStatus.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def directory(self):
        """Gets the directory of this AccountStatus.  # noqa: E501


        :return: The directory of this AccountStatus.  # noqa: E501
        :rtype: AccountStatusDirectory
        """
        return self._directory

    @directory.setter
    def directory(self, directory):
        """Sets the directory of this AccountStatus.


        :param directory: The directory of this AccountStatus.  # noqa: E501
        :type: AccountStatusDirectory
        """

        self._directory = directory

    @property
    def directory_id(self):
        """Gets the directory_id of this AccountStatus.  # noqa: E501


        :return: The directory_id of this AccountStatus.  # noqa: E501
        :rtype: str
        """
        return self._directory_id

    @directory_id.setter
    def directory_id(self, directory_id):
        """Sets the directory_id of this AccountStatus.


        :param directory_id: The directory_id of this AccountStatus.  # noqa: E501
        :type: str
        """

        self._directory_id = directory_id

    @property
    def status(self):
        """Gets the status of this AccountStatus.  # noqa: E501


        :return: The status of this AccountStatus.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AccountStatus.


        :param status: The status of this AccountStatus.  # noqa: E501
        :type: str
        """
        allowed_values = ["active", "inactive"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def updated_at(self):
        """Gets the updated_at of this AccountStatus.  # noqa: E501


        :return: The updated_at of this AccountStatus.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this AccountStatus.


        :param updated_at: The updated_at of this AccountStatus.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

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
        if issubclass(AccountStatus, dict):
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
        if not isinstance(other, AccountStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
