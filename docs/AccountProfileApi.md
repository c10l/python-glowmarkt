# swagger_client.AccountProfileApi

All URIs are relative to *https://api.glowmarkt.com/api/v0-1/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_account_profile**](AccountProfileApi.md#add_account_profile) | **POST** /accountprofile | Create an account profile under a given profileName.
[**get_account_profile**](AccountProfileApi.md#get_account_profile) | **GET** /accountprofile | Find all the profiles of an account
[**get_account_profileby_profile_name**](AccountProfileApi.md#get_account_profileby_profile_name) | **GET** /accountprofile/{profileName} | Find specific group of application

# **add_account_profile**
> InlineResponse2004 add_account_profile(body=body)

Create an account profile under a given profileName.

Create an account profile under a given profileName. profileName is a required field. Please note that anything under the profileName will be overwritten.

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
api_instance = swagger_client.AccountProfileApi(swagger_client.ApiClient(configuration))
body = swagger_client.AccountProfile() # AccountProfile | The information that is used to create a devuser. (optional)

try:
    # Create an account profile under a given profileName.
    api_response = api_instance.add_account_profile(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountProfileApi->add_account_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AccountProfile**](AccountProfile.md)| The information that is used to create a devuser. | [optional] 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[applicationId](../README.md#applicationId), [userToken](../README.md#userToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_profile**
> InlineResponse2003 get_account_profile()

Find all the profiles of an account

Returns all the profileNames of profiles an account has saved.

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
api_instance = swagger_client.AccountProfileApi(swagger_client.ApiClient(configuration))

try:
    # Find all the profiles of an account
    api_response = api_instance.get_account_profile()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountProfileApi->get_account_profile: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[applicationId](../README.md#applicationId), [userToken](../README.md#userToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_profileby_profile_name**
> AccountProfile get_account_profileby_profile_name(profile_name)

Find specific group of application

Returns an application's group.

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
api_instance = swagger_client.AccountProfileApi(swagger_client.ApiClient(configuration))
profile_name = 'profile_name_example' # str | profileName of the system to be retrieved

try:
    # Find specific group of application
    api_response = api_instance.get_account_profileby_profile_name(profile_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountProfileApi->get_account_profileby_profile_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_name** | **str**| profileName of the system to be retrieved | 

### Return type

[**AccountProfile**](AccountProfile.md)

### Authorization

[applicationId](../README.md#applicationId), [userToken](../README.md#userToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

