# coding: utf-8

"""
Glowmarkt User System

The document enlists and describes the APIs for the User.  # noqa: E501

OpenAPI spec version: 1.0.5

Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from python_glowmarkt.api_client import ApiClient


class AuthApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_token(self, **kwargs):  # noqa: E501
        """delete a token  # noqa: E501

        Delete the token the account used to make this call.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_token(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse2001
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.delete_token_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.delete_token_with_http_info(**kwargs)  # noqa: E501
            return data

    def delete_token_with_http_info(self, **kwargs):  # noqa: E501
        """delete a token  # noqa: E501

        Delete the token the account used to make this call.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_token_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse2001
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_token" % key
                )
            params[key] = val
        del params["kwargs"]

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["applicationId", "userToken"]  # noqa: E501

        return self.api_client.call_api(
            "/auth/deleteToken",
            "DELETE",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="InlineResponse2001",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def delete_token_by_id(self, token_id, **kwargs):  # noqa: E501
        """Deletes a token, specified by its tokenId.  # noqa: E501

        This call enables an user to delete and token and revoke access. JWT as well as OAuth tokens can be deleted.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_token_by_id(token_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str token_id: GUID of token that is to be deleted (required)
        :return: list[IsValidRes]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.delete_token_by_id_with_http_info(token_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_token_by_id_with_http_info(token_id, **kwargs)  # noqa: E501
            return data

    def delete_token_by_id_with_http_info(self, token_id, **kwargs):  # noqa: E501
        """Deletes a token, specified by its tokenId.  # noqa: E501

        This call enables an user to delete and token and revoke access. JWT as well as OAuth tokens can be deleted.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_token_by_id_with_http_info(token_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str token_id: GUID of token that is to be deleted (required)
        :return: list[IsValidRes]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["token_id"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_token_by_id" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'token_id' is set
        if "token_id" not in params or params["token_id"] is None:
            raise ValueError(
                "Missing the required parameter `token_id` when calling `delete_token_by_id`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "token_id" in params:
            path_params["tokenId"] = params["token_id"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["applicationId", "userToken"]  # noqa: E501

        return self.api_client.call_api(
            "/auth/token/{tokenId}",
            "DELETE",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="list[IsValidRes]",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def get_token_of_user(self, **kwargs):  # noqa: E501
        """Returns all the tokens that are active and valid for a specified user.  # noqa: E501

        This call enables a customer to view all the tokens that have been generated and used for their accounts. This includes all the JWT and OAuth tokens. By enabling this a user can then manage and monitor the access to their accounts.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_token_of_user(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[TokenDocument]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.get_token_of_user_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_token_of_user_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_token_of_user_with_http_info(self, **kwargs):  # noqa: E501
        """Returns all the tokens that are active and valid for a specified user.  # noqa: E501

        This call enables a customer to view all the tokens that have been generated and used for their accounts. This includes all the JWT and OAuth tokens. By enabling this a user can then manage and monitor the access to their accounts.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_token_of_user_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[TokenDocument]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_token_of_user" % key
                )
            params[key] = val
        del params["kwargs"]

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["applicationId", "userToken"]  # noqa: E501

        return self.api_client.call_api(
            "/auth/token",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="list[TokenDocument]",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def new_token(self, **kwargs):  # noqa: E501
        """Generate a new token for an account.  # noqa: E501

        An account provides an old token and gets a new one generated.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.new_token(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse2009
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.new_token_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.new_token_with_http_info(**kwargs)  # noqa: E501
            return data

    def new_token_with_http_info(self, **kwargs):  # noqa: E501
        """Generate a new token for an account.  # noqa: E501

        An account provides an old token and gets a new one generated.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.new_token_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse2009
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s' to method new_token" % key
                )
            params[key] = val
        del params["kwargs"]

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["applicationId", "userToken"]  # noqa: E501

        return self.api_client.call_api(
            "/auth/newToken",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="InlineResponse2009",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def usernamelogin(self, body, application_id, **kwargs):  # noqa: E501
        """authenticate an account  # noqa: E501

        Autheticates the user and generates a JWT token.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.usernamelogin(body, application_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UserNameLoginReq body: The information that is required to authenticate an account. (required)
        :param str application_id: The ID of the application (required)
        :return: InlineResponse2008
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.usernamelogin_with_http_info(body, application_id, **kwargs)  # noqa: E501
        else:
            (data) = self.usernamelogin_with_http_info(body, application_id, **kwargs)  # noqa: E501
            return data

    def usernamelogin_with_http_info(self, body, application_id, **kwargs):  # noqa: E501
        """authenticate an account  # noqa: E501

        Autheticates the user and generates a JWT token.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.usernamelogin_with_http_info(body, application_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UserNameLoginReq body: The information that is required to authenticate an account. (required)
        :param str application_id: The ID of the application (required)
        :return: InlineResponse2008
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["body", "application_id"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method usernamelogin" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'body' is set
        if "body" not in params or params["body"] is None:
            raise ValueError(
                "Missing the required parameter `body` when calling `usernamelogin`"
            )  # noqa: E501
        # verify the required parameter 'application_id' is set
        if "application_id" not in params or params["application_id"] is None:
            raise ValueError(
                "Missing the required parameter `application_id` when calling `usernamelogin`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if "application_id" in params:
            header_params["applicationId"] = params["application_id"]  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if "body" in params:
            body_params = params["body"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # HTTP header `Content-Type`
        header_params["Content-Type"] = self.api_client.select_header_content_type(  # noqa: E501
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            "/auth",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="InlineResponse2008",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )
