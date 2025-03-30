# swagger_client.AccountApi

All URIs are relative to *https://api.glowmarkt.com/api/v0-1/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**account_account_id_mobileapptoken_post**](AccountApi.md#account_account_id_mobileapptoken_post) | **POST** /account/{accountId}/mobileapptoken | Add mobile app token to a user
[**account_account_id_mobileapptoken_put**](AccountApi.md#account_account_id_mobileapptoken_put) | **PUT** /account/{accountId}/mobileapptoken | Remove a mobile app token to a user
[**add_account**](AccountApi.md#add_account) | **POST** /account | Add an account to an existing user
[**delete_account**](AccountApi.md#delete_account) | **DELETE** /account/{accountId} | Delete account
[**get_account_statusby_id**](AccountApi.md#get_account_statusby_id) | **GET** /account/{accountId}/status | Find the status of a specified account. If the account is using an external directory service, this call will confirm whether the user is authenticated against it. This call requires administrative application level credentials.
[**get_account_statusby_user_token**](AccountApi.md#get_account_statusby_user_token) | **GET** /account/status | With a given JWT token a user can have their account status verfied. If their account is created under an external directory service, this call will establish whether a user&#x27;s token to the external service is still valid.
[**get_accountby_id**](AccountApi.md#get_accountby_id) | **GET** /account/{accountId} | Find specific account of an application.
[**get_accounts**](AccountApi.md#get_accounts) | **GET** /account | Find all accounts of an application
[**update_account**](AccountApi.md#update_account) | **PUT** /account/{accountId} | Updates the account&#x27;s metadata.
[**user_change_email**](AccountApi.md#user_change_email) | **POST** /account/email | Change a user&#x27;s email
[**user_change_name**](AccountApi.md#user_change_name) | **POST** /account/name | Change a user&#x27;s name
[**user_change_pass_word**](AccountApi.md#user_change_pass_word) | **POST** /account/changepassword | Change a user&#x27;s password

# **account_account_id_mobileapptoken_post**
> InlineResponse2001 account_account_id_mobileapptoken_post(account_id, body=body)

Add mobile app token to a user

Mobile app token can be added to the user, who will then be able to receive push notifications.

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
api_instance = swagger_client.AccountApi(swagger_client.ApiClient(configuration))
account_id = 'account_id_example' # str | ID of account that is being queried
body = swagger_client.AddMobileTokenToAccountReq() # AddMobileTokenToAccountReq | The information that is needed to assign a mobile token to an account. (optional)

try:
    # Add mobile app token to a user
    api_response = api_instance.account_account_id_mobileapptoken_post(account_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->account_account_id_mobileapptoken_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| ID of account that is being queried | 
 **body** | [**AddMobileTokenToAccountReq**](AddMobileTokenToAccountReq.md)| The information that is needed to assign a mobile token to an account. | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[applicationId](../README.md#applicationId), [userToken](../README.md#userToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_account_id_mobileapptoken_put**
> InlineResponse2001 account_account_id_mobileapptoken_put(account_id, body=body)

Remove a mobile app token to a user

Mobile app tokens can be removed from a user.

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
api_instance = swagger_client.AccountApi(swagger_client.ApiClient(configuration))
account_id = 'account_id_example' # str | ID of account that is being queried
body = swagger_client.RemoveMobileTokenToAccountReq() # RemoveMobileTokenToAccountReq | The information that is needed to remove a mobile token to an account. (optional)

try:
    # Remove a mobile app token to a user
    api_response = api_instance.account_account_id_mobileapptoken_put(account_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->account_account_id_mobileapptoken_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| ID of account that is being queried | 
 **body** | [**RemoveMobileTokenToAccountReq**](RemoveMobileTokenToAccountReq.md)| The information that is needed to remove a mobile token to an account. | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[applicationId](../README.md#applicationId), [userToken](../README.md#userToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_account**
> InlineResponse200 add_account(body=body)

Add an account to an existing user

This call should be used when a user is registered via  on the Glow ecosystem. By providing the username of the user a directory account may be added to the application.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: appKeys
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: applicationId
configuration = swagger_client.Configuration()
configuration.api_key['applicationId'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['applicationId'] = 'Bearer'
# Configure API key authorization: devUserToken
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'# Configure HTTP basic authorization: orgAppKeys
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.AccountApi(swagger_client.ApiClient(configuration))
body = swagger_client.AddAccountReq() # AddAccountReq | The information that is used to add an account to an existing user. (optional)

try:
    # Add an account to an existing user
    api_response = api_instance.add_account(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->add_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddAccountReq**](AddAccountReq.md)| The information that is used to add an account to an existing user. | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[appKeys](../README.md#appKeys), [applicationId](../README.md#applicationId), [devUserToken](../README.md#devUserToken), [orgAppKeys](../README.md#orgAppKeys)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_account**
> InlineResponse2002 delete_account(account_id)

Delete account

Delete account

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: appKeys
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: devUserToken
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'# Configure HTTP basic authorization: orgAppKeys
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.AccountApi(swagger_client.ApiClient(configuration))
account_id = 'account_id_example' # str | ID of account that is to be deleted

try:
    # Delete account
    api_response = api_instance.delete_account(account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->delete_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| ID of account that is to be deleted | 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[appKeys](../README.md#appKeys), [devUserToken](../README.md#devUserToken), [orgAppKeys](../README.md#orgAppKeys)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_statusby_id**
> AccountStatus get_account_statusby_id(account_id)

Find the status of a specified account. If the account is using an external directory service, this call will confirm whether the user is authenticated against it. This call requires administrative application level credentials.

Returns the status an account.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: appKeys
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: applicationId
configuration = swagger_client.Configuration()
configuration.api_key['applicationId'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['applicationId'] = 'Bearer'
# Configure API key authorization: devUserToken
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'# Configure HTTP basic authorization: orgAppKeys
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.AccountApi(swagger_client.ApiClient(configuration))
account_id = 'account_id_example' # str | ID of account that is being queried

try:
    # Find the status of a specified account. If the account is using an external directory service, this call will confirm whether the user is authenticated against it. This call requires administrative application level credentials.
    api_response = api_instance.get_account_statusby_id(account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->get_account_statusby_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| ID of account that is being queried | 

### Return type

[**AccountStatus**](AccountStatus.md)

### Authorization

[appKeys](../README.md#appKeys), [applicationId](../README.md#applicationId), [devUserToken](../README.md#devUserToken), [orgAppKeys](../README.md#orgAppKeys)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_statusby_user_token**
> AccountStatus get_account_statusby_user_token()

With a given JWT token a user can have their account status verfied. If their account is created under an external directory service, this call will establish whether a user's token to the external service is still valid.

Returns the status an account.

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
api_instance = swagger_client.AccountApi(swagger_client.ApiClient(configuration))

try:
    # With a given JWT token a user can have their account status verfied. If their account is created under an external directory service, this call will establish whether a user's token to the external service is still valid.
    api_response = api_instance.get_account_statusby_user_token()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->get_account_statusby_user_token: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AccountStatus**](AccountStatus.md)

### Authorization

[applicationId](../README.md#applicationId), [userToken](../README.md#userToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_accountby_id**
> AccountRes get_accountby_id(account_id)

Find specific account of an application.

Returns an account.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: appKeys
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: applicationId
configuration = swagger_client.Configuration()
configuration.api_key['applicationId'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['applicationId'] = 'Bearer'
# Configure API key authorization: devUserToken
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'# Configure HTTP basic authorization: orgAppKeys
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.AccountApi(swagger_client.ApiClient(configuration))
account_id = 'account_id_example' # str | ID of account that is being queried

try:
    # Find specific account of an application.
    api_response = api_instance.get_accountby_id(account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->get_accountby_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| ID of account that is being queried | 

### Return type

[**AccountRes**](AccountRes.md)

### Authorization

[appKeys](../README.md#appKeys), [applicationId](../README.md#applicationId), [devUserToken](../README.md#devUserToken), [orgAppKeys](../README.md#orgAppKeys)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_accounts**
> list[AccountRes] get_accounts()

Find all accounts of an application

Returns all accounts that belong to an application.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: appKeys
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: applicationId
configuration = swagger_client.Configuration()
configuration.api_key['applicationId'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['applicationId'] = 'Bearer'
# Configure API key authorization: devUserToken
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'# Configure HTTP basic authorization: orgAppKeys
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.AccountApi(swagger_client.ApiClient(configuration))

try:
    # Find all accounts of an application
    api_response = api_instance.get_accounts()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->get_accounts: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[AccountRes]**](AccountRes.md)

### Authorization

[appKeys](../README.md#appKeys), [applicationId](../README.md#applicationId), [devUserToken](../README.md#devUserToken), [orgAppKeys](../README.md#orgAppKeys)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_account**
> UpdateAccountRes update_account(account_id, body=body)

Updates the account's metadata.

Updates the account s metadata. Elements that can be updated include name. This can be used in on an administrative level.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: appKeys
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: applicationId
configuration = swagger_client.Configuration()
configuration.api_key['applicationId'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['applicationId'] = 'Bearer'
# Configure API key authorization: devUserToken
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'# Configure HTTP basic authorization: orgAppKeys
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.AccountApi(swagger_client.ApiClient(configuration))
account_id = 'account_id_example' # str | ID of user that needs to be updated
body = swagger_client.AccountAccountIdBody() # AccountAccountIdBody | The elements of user that can be updated. (optional)

try:
    # Updates the account's metadata.
    api_response = api_instance.update_account(account_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->update_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| ID of user that needs to be updated | 
 **body** | [**AccountAccountIdBody**](AccountAccountIdBody.md)| The elements of user that can be updated. | [optional] 

### Return type

[**UpdateAccountRes**](UpdateAccountRes.md)

### Authorization

[appKeys](../README.md#appKeys), [applicationId](../README.md#applicationId), [devUserToken](../README.md#devUserToken), [orgAppKeys](../README.md#orgAppKeys)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_change_email**
> InlineResponse2001 user_change_email(body=body)

Change a user's email

A user can update their email

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
api_instance = swagger_client.AccountApi(swagger_client.ApiClient(configuration))
body = swagger_client.AccountEmailBody() # AccountEmailBody | The body contains the user's new email. (optional)

try:
    # Change a user's email
    api_response = api_instance.user_change_email(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->user_change_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AccountEmailBody**](AccountEmailBody.md)| The body contains the user&#x27;s new email. | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[applicationId](../README.md#applicationId), [userToken](../README.md#userToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_change_name**
> InlineResponse2001 user_change_name(body=body)

Change a user's name

A user can update their name

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
api_instance = swagger_client.AccountApi(swagger_client.ApiClient(configuration))
body = swagger_client.AccountNameBody() # AccountNameBody | The body contains the user's new email. (optional)

try:
    # Change a user's name
    api_response = api_instance.user_change_name(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->user_change_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AccountNameBody**](AccountNameBody.md)| The body contains the user&#x27;s new email. | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[applicationId](../README.md#applicationId), [userToken](../README.md#userToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_change_pass_word**
> InlineResponse2001 user_change_pass_word(body=body)

Change a user's password

A user can change their passwrod. They would neeed to have knowledge of their previous password and provide it in the body.

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
api_instance = swagger_client.AccountApi(swagger_client.ApiClient(configuration))
body = swagger_client.AccountChangepasswordBody() # AccountChangepasswordBody | The information that is needed to change a user's password. (optional)

try:
    # Change a user's password
    api_response = api_instance.user_change_pass_word(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->user_change_pass_word: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AccountChangepasswordBody**](AccountChangepasswordBody.md)| The information that is needed to change a user&#x27;s password. | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[applicationId](../README.md#applicationId), [userToken](../README.md#userToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

