# swagger_client.AuthApi

All URIs are relative to *https://api.glowmarkt.com/api/v0-1/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_token**](AuthApi.md#delete_token) | **DELETE** /auth/deleteToken | delete a token
[**delete_token_by_id**](AuthApi.md#delete_token_by_id) | **DELETE** /auth/token/{tokenId} | Deletes a token, specified by its tokenId.
[**get_token_of_user**](AuthApi.md#get_token_of_user) | **GET** /auth/token | Returns all the tokens that are active and valid for a specified user.
[**new_token**](AuthApi.md#new_token) | **GET** /auth/newToken | Generate a new token for an account.
[**usernamelogin**](AuthApi.md#usernamelogin) | **POST** /auth | authenticate an account

# **delete_token**
> InlineResponse2001 delete_token()

delete a token

Delete the token the account used to make this call.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: applicationId
configuration = swagger_client.Configuration()
configuration.api_key['applicationId'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['applicationId'] = 'Bearer'
# Configure API key authorization: userToken
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.AuthApi(swagger_client.ApiClient(configuration))

try:
    # delete a token
    api_response = api_instance.delete_token()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->delete_token: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[applicationId](../README.md#applicationId), [userToken](../README.md#userToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_token_by_id**
> list[IsValidRes] delete_token_by_id(token_id)

Deletes a token, specified by its tokenId.

This call enables an user to delete and token and revoke access. JWT as well as OAuth tokens can be deleted.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: applicationId
configuration = swagger_client.Configuration()
configuration.api_key['applicationId'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['applicationId'] = 'Bearer'
# Configure API key authorization: userToken
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.AuthApi(swagger_client.ApiClient(configuration))
token_id = 'token_id_example' # str | GUID of token that is to be deleted

try:
    # Deletes a token, specified by its tokenId.
    api_response = api_instance.delete_token_by_id(token_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->delete_token_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_id** | **str**| GUID of token that is to be deleted | 

### Return type

[**list[IsValidRes]**](IsValidRes.md)

### Authorization

[applicationId](../README.md#applicationId), [userToken](../README.md#userToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_token_of_user**
> list[TokenDocument] get_token_of_user()

Returns all the tokens that are active and valid for a specified user.

This call enables a customer to view all the tokens that have been generated and used for their accounts. This includes all the JWT and OAuth tokens. By enabling this a user can then manage and monitor the access to their accounts.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: applicationId
configuration = swagger_client.Configuration()
configuration.api_key['applicationId'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['applicationId'] = 'Bearer'
# Configure API key authorization: userToken
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.AuthApi(swagger_client.ApiClient(configuration))

try:
    # Returns all the tokens that are active and valid for a specified user.
    api_response = api_instance.get_token_of_user()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->get_token_of_user: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[TokenDocument]**](TokenDocument.md)

### Authorization

[applicationId](../README.md#applicationId), [userToken](../README.md#userToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **new_token**
> InlineResponse2009 new_token()

Generate a new token for an account.

An account provides an old token and gets a new one generated.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: applicationId
configuration = swagger_client.Configuration()
configuration.api_key['applicationId'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['applicationId'] = 'Bearer'
# Configure API key authorization: userToken
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.AuthApi(swagger_client.ApiClient(configuration))

try:
    # Generate a new token for an account.
    api_response = api_instance.new_token()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->new_token: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

[applicationId](../README.md#applicationId), [userToken](../README.md#userToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **usernamelogin**
> InlineResponse2008 usernamelogin(body, application_id)

authenticate an account

Autheticates the user and generates a JWT token.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthApi()
body = swagger_client.UserNameLoginReq() # UserNameLoginReq | The information that is required to authenticate an account.
application_id = 'application_id_example' # str | The ID of the application

try:
    # authenticate an account
    api_response = api_instance.usernamelogin(body, application_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->usernamelogin: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserNameLoginReq**](UserNameLoginReq.md)| The information that is required to authenticate an account. | 
 **application_id** | **str**| The ID of the application | 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

