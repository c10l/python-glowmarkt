# swagger_client.AccountsessionApi

All URIs are relative to *https://api.glowmarkt.com/api/v0-1/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**update_account_session**](AccountsessionApi.md#update_account_session) | **PUT** /accountsession | Update an account session.

# **update_account_session**
> InlineResponse2006 update_account_session(body=body)

Update an account session.

Update fields of an account session. The fields that are updated are completely overwritten if they exist.

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
api_instance = swagger_client.AccountsessionApi(swagger_client.ApiClient(configuration))
body = swagger_client.AccountSession() # AccountSession | The information that is used to create a devuser. (optional)

try:
    # Update an account session.
    api_response = api_instance.update_account_session(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsessionApi->update_account_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AccountSession**](AccountSession.md)| The information that is used to create a devuser. | [optional] 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

[applicationId](../README.md#applicationId), [userToken](../README.md#userToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

