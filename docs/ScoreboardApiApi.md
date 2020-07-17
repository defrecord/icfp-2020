# swagger_client.ScoreboardApiApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**scoreboard_lightning_get**](ScoreboardApiApi.md#scoreboard_lightning_get) | **GET** /scoreboard/lightning | 

# **scoreboard_lightning_get**
> LightningScoreboardDto scoreboard_lightning_get()



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
api_instance = swagger_client.ScoreboardApiApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.scoreboard_lightning_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScoreboardApiApi->scoreboard_lightning_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**LightningScoreboardDto**](LightningScoreboardDto.md)

### Authorization

[ICFPC-ApiKey](../README.md#ICFPC-ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

