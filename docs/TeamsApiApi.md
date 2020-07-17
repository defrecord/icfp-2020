# swagger_client.TeamsApiApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**teams_current_get**](TeamsApiApi.md#teams_current_get) | **GET** /teams/current | 

# **teams_current_get**
> RegisteredTeamDto teams_current_get()



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
api_instance = swagger_client.TeamsApiApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.teams_current_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApiApi->teams_current_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**RegisteredTeamDto**](RegisteredTeamDto.md)

### Authorization

[ICFPC-ApiKey](../README.md#ICFPC-ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

