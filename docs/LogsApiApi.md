# swagger_client.LogsApiApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**logs_get**](LogsApiApi.md#logs_get) | **GET** /logs | 

# **logs_get**
> logs_get(log_key)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ICFPC-ApiKey
configuration = swagger_client.Configuration()
configuration.api_key['apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.LogsApiApi(swagger_client.ApiClient(configuration))
log_key = 'log_key_example' # str | 

try:
    api_instance.logs_get(log_key)
except ApiException as e:
    print("Exception when calling LogsApiApi->logs_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **log_key** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[ICFPC-ApiKey](../README.md#ICFPC-ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

