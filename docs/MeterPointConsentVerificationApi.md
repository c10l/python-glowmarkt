# swagger_client.MeterPointConsentVerificationApi

All URIs are relative to *https://api.glowmarkt.com/api/v0-1/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_meter_point_consent_renewal**](MeterPointConsentVerificationApi.md#get_meter_point_consent_renewal) | **GET** /user/verification/status/mpxn/{mpxn}/renewal | Get meter point consent renewals
[**get_meter_point_consent_revocation**](MeterPointConsentVerificationApi.md#get_meter_point_consent_revocation) | **GET** /user/verification/status/mpxn/{mpxn}/revocation | Get meter point consent revocations
[**get_user_meter_point_verification_consent_status**](MeterPointConsentVerificationApi.md#get_user_meter_point_verification_consent_status) | **GET** /user/verification/status | API to retrieve user&#x27;s meter points&#x27; consent and verification
[**renew_meter_point_consent**](MeterPointConsentVerificationApi.md#renew_meter_point_consent) | **POST** /user/verification/status/mpxn/{mpxn}/renewal | Renew meter point consent
[**renew_meter_point_consent_bulk**](MeterPointConsentVerificationApi.md#renew_meter_point_consent_bulk) | **POST** /user/verification/status/mpxns/renewal | Renew consent for a number of meterpoints
[**renew_meter_point_consent_revoke_bulk**](MeterPointConsentVerificationApi.md#renew_meter_point_consent_revoke_bulk) | **POST** /user/verification/status/mpxns/revocation | Revoke consent for a number of meterpoints
[**revoke_meter_point_consent**](MeterPointConsentVerificationApi.md#revoke_meter_point_consent) | **POST** /user/verification/status/mpxn/{mpxn}/revocation | Revoke meter point consent

# **get_meter_point_consent_renewal**
> MeterPointConsentAndVerificationRenewalRes get_meter_point_consent_renewal(mpxn)

Get meter point consent renewals

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
# Configure API key authorization: userId
configuration = swagger_client.Configuration()
configuration.api_key['userId'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userId'] = 'Bearer'
# Configure API key authorization: userToken
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.MeterPointConsentVerificationApi(swagger_client.ApiClient(configuration))
mpxn = 'mpxn_example' # str | meter point number

try:
    # Get meter point consent renewals
    api_response = api_instance.get_meter_point_consent_renewal(mpxn)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeterPointConsentVerificationApi->get_meter_point_consent_renewal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mpxn** | **str**| meter point number | 

### Return type

[**MeterPointConsentAndVerificationRenewalRes**](MeterPointConsentAndVerificationRenewalRes.md)

### Authorization

[appKeys](../README.md#appKeys), [applicationId](../README.md#applicationId), [devUserToken](../README.md#devUserToken), [orgAppKeys](../README.md#orgAppKeys), [userId](../README.md#userId), [userToken](../README.md#userToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_meter_point_consent_revocation**
> MeterPointConsentAndVerificationRenewalRes get_meter_point_consent_revocation(mpxn)

Get meter point consent revocations

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
# Configure API key authorization: userId
configuration = swagger_client.Configuration()
configuration.api_key['userId'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userId'] = 'Bearer'
# Configure API key authorization: userToken
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.MeterPointConsentVerificationApi(swagger_client.ApiClient(configuration))
mpxn = 'mpxn_example' # str | meter point number

try:
    # Get meter point consent revocations
    api_response = api_instance.get_meter_point_consent_revocation(mpxn)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeterPointConsentVerificationApi->get_meter_point_consent_revocation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mpxn** | **str**| meter point number | 

### Return type

[**MeterPointConsentAndVerificationRenewalRes**](MeterPointConsentAndVerificationRenewalRes.md)

### Authorization

[appKeys](../README.md#appKeys), [applicationId](../README.md#applicationId), [devUserToken](../README.md#devUserToken), [orgAppKeys](../README.md#orgAppKeys), [userId](../README.md#userId), [userToken](../README.md#userToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_meter_point_verification_consent_status**
> UserMeterPointConsentAndVerification get_user_meter_point_verification_consent_status()

API to retrieve user's meter points' consent and verification

API to retrieve user's meter points' consent and verification status

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
# Configure API key authorization: userId
configuration = swagger_client.Configuration()
configuration.api_key['userId'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userId'] = 'Bearer'
# Configure API key authorization: userToken
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.MeterPointConsentVerificationApi(swagger_client.ApiClient(configuration))

try:
    # API to retrieve user's meter points' consent and verification
    api_response = api_instance.get_user_meter_point_verification_consent_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeterPointConsentVerificationApi->get_user_meter_point_verification_consent_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UserMeterPointConsentAndVerification**](UserMeterPointConsentAndVerification.md)

### Authorization

[appKeys](../README.md#appKeys), [applicationId](../README.md#applicationId), [devUserToken](../README.md#devUserToken), [orgAppKeys](../README.md#orgAppKeys), [userId](../README.md#userId), [userToken](../README.md#userToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **renew_meter_point_consent**
> AddUserRes renew_meter_point_consent(mpxn, body=body)

Renew meter point consent

A user can renew their consent to access a meter point's data. The consent can be extended to a maximum of 18 months (default).

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
# Configure API key authorization: userId
configuration = swagger_client.Configuration()
configuration.api_key['userId'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userId'] = 'Bearer'
# Configure API key authorization: userToken
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.MeterPointConsentVerificationApi(swagger_client.ApiClient(configuration))
mpxn = 'mpxn_example' # str | meter point number
body = swagger_client.RenewMeterPointConsentReq() # RenewMeterPointConsentReq |  (optional)

try:
    # Renew meter point consent
    api_response = api_instance.renew_meter_point_consent(mpxn, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeterPointConsentVerificationApi->renew_meter_point_consent: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mpxn** | **str**| meter point number | 
 **body** | [**RenewMeterPointConsentReq**](RenewMeterPointConsentReq.md)|  | [optional] 

### Return type

[**AddUserRes**](AddUserRes.md)

### Authorization

[appKeys](../README.md#appKeys), [applicationId](../README.md#applicationId), [devUserToken](../README.md#devUserToken), [orgAppKeys](../README.md#orgAppKeys), [userId](../README.md#userId), [userToken](../README.md#userToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **renew_meter_point_consent_bulk**
> MeterPointConsentManagementBulkRenewalRes renew_meter_point_consent_bulk(body=body)

Renew consent for a number of meterpoints

A user can renew their consent for a number of meterpoints.  The consent can be extended to a maximum of 18 months (default).

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
# Configure API key authorization: userId
configuration = swagger_client.Configuration()
configuration.api_key['userId'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userId'] = 'Bearer'
# Configure API key authorization: userToken
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.MeterPointConsentVerificationApi(swagger_client.ApiClient(configuration))
body = swagger_client.MeterPointConsentManagementBulkReq() # MeterPointConsentManagementBulkReq |  (optional)

try:
    # Renew consent for a number of meterpoints
    api_response = api_instance.renew_meter_point_consent_bulk(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeterPointConsentVerificationApi->renew_meter_point_consent_bulk: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MeterPointConsentManagementBulkReq**](MeterPointConsentManagementBulkReq.md)|  | [optional] 

### Return type

[**MeterPointConsentManagementBulkRenewalRes**](MeterPointConsentManagementBulkRenewalRes.md)

### Authorization

[appKeys](../README.md#appKeys), [applicationId](../README.md#applicationId), [devUserToken](../README.md#devUserToken), [orgAppKeys](../README.md#orgAppKeys), [userId](../README.md#userId), [userToken](../README.md#userToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **renew_meter_point_consent_revoke_bulk**
> MeterPointConsentManagementBulkRevocationRes renew_meter_point_consent_revoke_bulk(body=body)

Revoke consent for a number of meterpoints

A user can revoke their consent for a number of meterpoints.

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
# Configure API key authorization: userId
configuration = swagger_client.Configuration()
configuration.api_key['userId'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userId'] = 'Bearer'
# Configure API key authorization: userToken
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.MeterPointConsentVerificationApi(swagger_client.ApiClient(configuration))
body = swagger_client.MeterPointConsentManagementBulkReq() # MeterPointConsentManagementBulkReq |  (optional)

try:
    # Revoke consent for a number of meterpoints
    api_response = api_instance.renew_meter_point_consent_revoke_bulk(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeterPointConsentVerificationApi->renew_meter_point_consent_revoke_bulk: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MeterPointConsentManagementBulkReq**](MeterPointConsentManagementBulkReq.md)|  | [optional] 

### Return type

[**MeterPointConsentManagementBulkRevocationRes**](MeterPointConsentManagementBulkRevocationRes.md)

### Authorization

[appKeys](../README.md#appKeys), [applicationId](../README.md#applicationId), [devUserToken](../README.md#devUserToken), [orgAppKeys](../README.md#orgAppKeys), [userId](../README.md#userId), [userToken](../README.md#userToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_meter_point_consent**
> AddUserRes revoke_meter_point_consent(mpxn, body=body)

Revoke meter point consent

A user can renew their consent to access a meter point's data. The consent can be extended to a maximum of 18 months (default).

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
# Configure API key authorization: userId
configuration = swagger_client.Configuration()
configuration.api_key['userId'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userId'] = 'Bearer'
# Configure API key authorization: userToken
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.MeterPointConsentVerificationApi(swagger_client.ApiClient(configuration))
mpxn = 'mpxn_example' # str | meter point number
body = swagger_client.RenewMeterPointConsentReq() # RenewMeterPointConsentReq |  (optional)

try:
    # Revoke meter point consent
    api_response = api_instance.revoke_meter_point_consent(mpxn, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeterPointConsentVerificationApi->revoke_meter_point_consent: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mpxn** | **str**| meter point number | 
 **body** | [**RenewMeterPointConsentReq**](RenewMeterPointConsentReq.md)|  | [optional] 

### Return type

[**AddUserRes**](AddUserRes.md)

### Authorization

[appKeys](../README.md#appKeys), [applicationId](../README.md#applicationId), [devUserToken](../README.md#devUserToken), [orgAppKeys](../README.md#orgAppKeys), [userId](../README.md#userId), [userToken](../README.md#userToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

