# swagger_client.AliensApiApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**aliens_response_id_get**](AliensApiApi.md#aliens_response_id_get) | **GET** /aliens/{responseId} | 
[**aliens_send_post**](AliensApiApi.md#aliens_send_post) | **POST** /aliens/send | 

# **aliens_response_id_get**
> aliens_response_id_get(response_id)



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
api_instance = swagger_client.AliensApiApi(swagger_client.ApiClient(configuration))
response_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    api_instance.aliens_response_id_get(response_id)
except ApiException as e:
    print("Exception when calling AliensApiApi->aliens_response_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **response_id** | [**str**](.md)|  | 

### Return type

void (empty response body)

### Authorization

[ICFPC-ApiKey](../README.md#ICFPC-ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **aliens_send_post**
> aliens_send_post(body=body)



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
api_instance = swagger_client.AliensApiApi(swagger_client.ApiClient(configuration))
body = 'body_example' # str |  (optional)

try:
    api_instance.aliens_send_post(body=body)
except ApiException as e:
    print("Exception when calling AliensApiApi->aliens_send_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[ICFPC-ApiKey](../README.md#ICFPC-ApiKey)

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

