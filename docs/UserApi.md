# python_glowmarkt.UserApi

All URIs are relative to *https://api.glowmarkt.com/api/v0-1/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_user**](UserApi.md#add_user) | **POST** /register | Create a user
[**create_user**](UserApi.md#create_user) | **POST** /user | Create a user
[**delete_userby_id**](UserApi.md#delete_userby_id) | **DELETE** /user/{userId} | Delete specific user. This will delete all the accounts of a user. Please refer to delete account API. This API requires specific permissions.
[**generate_user_password_reset_token**](UserApi.md#generate_user_password_reset_token) | **POST** /user/resetpassword | Generate a token that can be used by user to reset their password.
[**generate_user_verification_token**](UserApi.md#generate_user_verification_token) | **POST** /user/verify | Generate a user verification token
[**get_userby_id**](UserApi.md#get_userby_id) | **GET** /user/{userId} | Find specific user that has an account in an application.
[**get_userby_username**](UserApi.md#get_userby_username) | **GET** /user | Find specific user that has an account in an application from the username.
[**reset_password_user**](UserApi.md#reset_password_user) | **PUT** /user/resetpassword | A user resets their password
[**update_username_user_id**](UserApi.md#update_username_user_id) | **PUT** /user/{userId}/username | Change a user&#x27;s username
[**verify_user**](UserApi.md#verify_user) | **PUT** /user/verify | Verify a user verification token

# **add_user**
> AddUserRes add_user(body=body)

Create a user

Create a User a directory account for username and password login using this action. More specifically this is a registration process which creates a user and adds an account to the given application id. Self-Registration process should use this action. This call requires no authentication.

### Example
```python
from __future__ import print_function
import time
import python_glowmarkt
from python_glowmarkt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = python_glowmarkt.UserApi()
body = python_glowmarkt.AddUserReq() # AddUserReq | The information that is used to create a user. (optional)

try:
    # Create a user
    api_response = api_instance.add_user(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->add_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddUserReq**](AddUserReq.md)| The information that is used to create a user. | [optional]

### Return type

[**AddUserRes**](AddUserRes.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user**
> CreateUserRes create_user(body=body)

Create a user

This call can be used by an application to create a user. No verification will be required

### Example
```python
from __future__ import print_function
import time
import python_glowmarkt
from python_glowmarkt.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: appKeys
configuration = python_glowmarkt.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: applicationId
configuration = python_glowmarkt.Configuration()
configuration.api_key['applicationId'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['applicationId'] = 'Bearer'
# Configure API key authorization: devUserToken
configuration = python_glowmarkt.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'# Configure HTTP basic authorization: orgAppKeys
configuration = python_glowmarkt.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = python_glowmarkt.UserApi(python_glowmarkt.ApiClient(configuration))
body = python_glowmarkt.CreateUserReq() # CreateUserReq | The information that is used to create a user. (optional)

try:
    # Create a user
    api_response = api_instance.create_user(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->create_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateUserReq**](CreateUserReq.md)| The information that is used to create a user. | [optional]

### Return type

[**CreateUserRes**](CreateUserRes.md)

### Authorization

[appKeys](../README.md#appKeys), [applicationId](../README.md#applicationId), [devUserToken](../README.md#devUserToken), [orgAppKeys](../README.md#orgAppKeys)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_userby_id**
> IsValidRes delete_userby_id(user_id)

Delete specific user. This will delete all the accounts of a user. Please refer to delete account API. This API requires specific permissions.

Deletes a user.

### Example
```python
from __future__ import print_function
import time
import python_glowmarkt
from python_glowmarkt.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: appKeys
configuration = python_glowmarkt.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: applicationId
configuration = python_glowmarkt.Configuration()
configuration.api_key['applicationId'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['applicationId'] = 'Bearer'
# Configure API key authorization: devUserToken
configuration = python_glowmarkt.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'# Configure HTTP basic authorization: orgAppKeys
configuration = python_glowmarkt.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = python_glowmarkt.UserApi(python_glowmarkt.ApiClient(configuration))
user_id = 'user_id_example' # str | ID of user that is being queried

try:
    # Delete specific user. This will delete all the accounts of a user. Please refer to delete account API. This API requires specific permissions.
    api_response = api_instance.delete_userby_id(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->delete_userby_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ID of user that is being queried |

### Return type

[**IsValidRes**](IsValidRes.md)

### Authorization

[appKeys](../README.md#appKeys), [applicationId](../README.md#applicationId), [devUserToken](../README.md#devUserToken), [orgAppKeys](../README.md#orgAppKeys)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_user_password_reset_token**
> InlineResponse2001 generate_user_password_reset_token(body=body)

Generate a token that can be used by user to reset their password.

This call generates a 4 digit token and sends it via second channel of communication over to the user (at the moment the only second channel of communication supported is email). The user can then use this token to reset their password.

### Example
```python
from __future__ import print_function
import time
import python_glowmarkt
from python_glowmarkt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = python_glowmarkt.UserApi()
body = python_glowmarkt.GeneratePasswordResetTokenUserReq() # GeneratePasswordResetTokenUserReq | The information that is needed to generate a password reset token. (optional)

try:
    # Generate a token that can be used by user to reset their password.
    api_response = api_instance.generate_user_password_reset_token(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->generate_user_password_reset_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GeneratePasswordResetTokenUserReq**](GeneratePasswordResetTokenUserReq.md)| The information that is needed to generate a password reset token. | [optional]

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_user_verification_token**
> InlineResponse2001 generate_user_verification_token(body=body)

Generate a user verification token

This call generates a 4 digit token and sends it via second channel of communication over to the user (at the moment the only second channel of communication supported is email).

### Example
```python
from __future__ import print_function
import time
import python_glowmarkt
from python_glowmarkt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = python_glowmarkt.UserApi()
body = python_glowmarkt.GenerateVerificationTokenUserReq() # GenerateVerificationTokenUserReq | The information that is used to create to generate an email verification token. (optional)

try:
    # Generate a user verification token
    api_response = api_instance.generate_user_verification_token(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->generate_user_verification_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GenerateVerificationTokenUserReq**](GenerateVerificationTokenUserReq.md)| The information that is used to create to generate an email verification token. | [optional]

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_userby_id**
> AddUserRes get_userby_id(user_id)

Find specific user that has an account in an application.

Returns a user.

### Example
```python
from __future__ import print_function
import time
import python_glowmarkt
from python_glowmarkt.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: appKeys
configuration = python_glowmarkt.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: applicationId
configuration = python_glowmarkt.Configuration()
configuration.api_key['applicationId'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['applicationId'] = 'Bearer'
# Configure API key authorization: devUserToken
configuration = python_glowmarkt.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'# Configure HTTP basic authorization: orgAppKeys
configuration = python_glowmarkt.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = python_glowmarkt.UserApi(python_glowmarkt.ApiClient(configuration))
user_id = 'user_id_example' # str | ID of user that is being queried

try:
    # Find specific user that has an account in an application.
    api_response = api_instance.get_userby_id(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_userby_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ID of user that is being queried |

### Return type

[**AddUserRes**](AddUserRes.md)

### Authorization

[appKeys](../README.md#appKeys), [applicationId](../README.md#applicationId), [devUserToken](../README.md#devUserToken), [orgAppKeys](../README.md#orgAppKeys)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_userby_username**
> AddUserRes get_userby_username(username)

Find specific user that has an account in an application from the username.

Returns a user.

### Example
```python
from __future__ import print_function
import time
import python_glowmarkt
from python_glowmarkt.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: appKeys
configuration = python_glowmarkt.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: applicationId
configuration = python_glowmarkt.Configuration()
configuration.api_key['applicationId'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['applicationId'] = 'Bearer'
# Configure API key authorization: devUserToken
configuration = python_glowmarkt.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'# Configure HTTP basic authorization: orgAppKeys
configuration = python_glowmarkt.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = python_glowmarkt.UserApi(python_glowmarkt.ApiClient(configuration))
username = 'username_example' # str | The username of user that is being queried (lowercase, trimmed etc). Please note that this API is prone to errors if the username contains characters that are affected by URL encoding.

try:
    # Find specific user that has an account in an application from the username.
    api_response = api_instance.get_userby_username(username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_userby_username: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The username of user that is being queried (lowercase, trimmed etc). Please note that this API is prone to errors if the username contains characters that are affected by URL encoding. |

### Return type

[**AddUserRes**](AddUserRes.md)

### Authorization

[appKeys](../README.md#appKeys), [applicationId](../README.md#applicationId), [devUserToken](../README.md#devUserToken), [orgAppKeys](../README.md#orgAppKeys)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_password_user**
> InlineResponse2001 reset_password_user(body=body)

A user resets their password

This call generates a 4 digit token and sends it via second channel of communication over to the user (at the moment the only second channel of communication supported is email).

### Example
```python
from __future__ import print_function
import time
import python_glowmarkt
from python_glowmarkt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = python_glowmarkt.UserApi()
body = python_glowmarkt.PasswordResetUserReq() # PasswordResetUserReq | The information that is used to reset a user's password. (optional)

try:
    # A user resets their password
    api_response = api_instance.reset_password_user(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->reset_password_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PasswordResetUserReq**](PasswordResetUserReq.md)| The information that is used to reset a user&#x27;s password. | [optional]

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_username_user_id**
> InlineResponse2001 update_username_user_id(user_id, body=body)

Change a user's username

API to update a user's username

### Example
```python
from __future__ import print_function
import time
import python_glowmarkt
from python_glowmarkt.rest import ApiException
from pprint import pprint

# Configure API key authorization: applicationId
configuration = python_glowmarkt.Configuration()
configuration.api_key['applicationId'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['applicationId'] = 'Bearer'
# Configure API key authorization: userToken
configuration = python_glowmarkt.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = python_glowmarkt.UserApi(python_glowmarkt.ApiClient(configuration))
user_id = 'user_id_example' # str | ID of user that is being queried
body = python_glowmarkt.UserIdUsernameBody() # UserIdUsernameBody | The body contains the user's new email. (optional)

try:
    # Change a user's username
    api_response = api_instance.update_username_user_id(user_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->update_username_user_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ID of user that is being queried |
 **body** | [**UserIdUsernameBody**](UserIdUsernameBody.md)| The body contains the user&#x27;s new email. | [optional]

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[applicationId](../README.md#applicationId), [userToken](../README.md#userToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_user**
> InlineResponse20010 verify_user(body=body)

Verify a user verification token

This call generates a 4 digit token and sends it via second channel of communication over to the user (at the moment the only second channel of communication supported is email).

### Example
```python
from __future__ import print_function
import time
import python_glowmarkt
from python_glowmarkt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = python_glowmarkt.UserApi()
body = python_glowmarkt.VerifyUserReq() # VerifyUserReq | The information that is used to create a devuser. (optional)

try:
    # Verify a user verification token
    api_response = api_instance.verify_user(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->verify_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VerifyUserReq**](VerifyUserReq.md)| The information that is used to create a devuser. | [optional]

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
