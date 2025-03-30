# swagger_client.OAuthApi

All URIs are relative to *https://api.glowmarkt.com/api/v0-1/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**exchange_authorization_code_with_access**](OAuthApi.md#exchange_authorization_code_with_access) | **POST** /auth/oauth/access | Exchange the Authorization Code for an Access Token.
[**generate_o_authorization_code**](OAuthApi.md#generate_o_authorization_code) | **POST** /auth/oauth | Authenticate a user and generate an OAuth 2.0 Authorization Code Grant.
[**validate_o_auth_access_token**](OAuthApi.md#validate_o_auth_access_token) | **GET** /auth/oauth | Check and validate an Oauth Access token.

# **exchange_authorization_code_with_access**
> ExchangeAuthorizationCodeWithAccessRes exchange_authorization_code_with_access(client_id, client_secret, code, grant_type)

Exchange the Authorization Code for an Access Token.

The user system supports an OAuth 2.0 Authorization Code Grant. This call generates an access and refresh token from an OAuth 2.0 Authorization Code Grant. This API can also be used to generate a new access token with a given refresh token. Instead of using the authorization code in the body of the request (code), use the refresh token (refresh_token).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OAuthApi()
client_id = true # bool | 
client_secret = 'client_secret_example' # str | 
code = 'code_example' # str | 
grant_type = 'grant_type_example' # str | 

try:
    # Exchange the Authorization Code for an Access Token.
    api_response = api_instance.exchange_authorization_code_with_access(client_id, client_secret, code, grant_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OAuthApi->exchange_authorization_code_with_access: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **bool**|  | 
 **client_secret** | **str**|  | 
 **code** | **str**|  | 
 **grant_type** | **str**|  | 

### Return type

[**ExchangeAuthorizationCodeWithAccessRes**](ExchangeAuthorizationCodeWithAccessRes.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_o_authorization_code**
> OAuthCodeRes generate_o_authorization_code(body, application_id)

Authenticate a user and generate an OAuth 2.0 Authorization Code Grant.

The user system supports an OAuth 2.0 Authorization Code Grant. This call authenticates a user and generates an OAuth 2.0 Authorization Code Grant.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OAuthApi()
body = swagger_client.UserNameLoginReq() # UserNameLoginReq | The information that is required to authenticate an account.
application_id = 'application_id_example' # str | The ID of the application

try:
    # Authenticate a user and generate an OAuth 2.0 Authorization Code Grant.
    api_response = api_instance.generate_o_authorization_code(body, application_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OAuthApi->generate_o_authorization_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserNameLoginReq**](UserNameLoginReq.md)| The information that is required to authenticate an account. | 
 **application_id** | **str**| The ID of the application | 

### Return type

[**OAuthCodeRes**](OAuthCodeRes.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_o_auth_access_token**
> OAuthValidAccessToken validate_o_auth_access_token()

Check and validate an Oauth Access token.

The user system supports an OAuth 2.0 Authorization Code Grant. This call validates that a generated access key is valid.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: oAccessAuthToken
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.OAuthApi(swagger_client.ApiClient(configuration))

try:
    # Check and validate an Oauth Access token.
    api_response = api_instance.validate_o_auth_access_token()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OAuthApi->validate_o_auth_access_token: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**OAuthValidAccessToken**](OAuthValidAccessToken.md)

### Authorization

[oAccessAuthToken](../README.md#oAccessAuthToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

