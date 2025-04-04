# coding: utf-8

"""
Glowmarkt User System

The document enlists and describes the APIs for the User.  # noqa: E501

OpenAPI spec version: 1.0.5

Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import python_glowmarkt
from python_glowmarkt.api.accountsession_api import AccountsessionApi  # noqa: E501
from python_glowmarkt.rest import ApiException


class TestAccountsessionApi(unittest.TestCase):
    """AccountsessionApi unit test stubs"""

    def setUp(self):
        self.api = AccountsessionApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_update_account_session(self):
        """Test case for update_account_session

        Update an account session.  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()
