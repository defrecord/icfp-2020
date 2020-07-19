# swagger_client.TournamentsApiApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tournaments_current_get**](TournamentsApiApi.md#tournaments_current_get) | **GET** /tournaments/current | 
[**tournaments_get**](TournamentsApiApi.md#tournaments_get) | **GET** /tournaments | 
[**tournaments_tournament_id_get**](TournamentsApiApi.md#tournaments_tournament_id_get) | **GET** /tournaments/{tournamentId} | 

# **tournaments_current_get**
> TournamentDto tournaments_current_get()



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
api_instance = swagger_client.TournamentsApiApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.tournaments_current_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TournamentsApiApi->tournaments_current_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TournamentDto**](TournamentDto.md)

### Authorization

[ICFPC-ApiKey](../README.md#ICFPC-ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tournaments_get**
> list[TournamentDto] tournaments_get()



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
api_instance = swagger_client.TournamentsApiApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.tournaments_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TournamentsApiApi->tournaments_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[TournamentDto]**](TournamentDto.md)

### Authorization

[ICFPC-ApiKey](../README.md#ICFPC-ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tournaments_tournament_id_get**
> TournamentDto tournaments_tournament_id_get(tournament_id)



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
api_instance = swagger_client.TournamentsApiApi(swagger_client.ApiClient(configuration))
tournament_id = 56 # int | 

try:
    api_response = api_instance.tournaments_tournament_id_get(tournament_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TournamentsApiApi->tournaments_tournament_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tournament_id** | **int**|  | 

### Return type

[**TournamentDto**](TournamentDto.md)

### Authorization

[ICFPC-ApiKey](../README.md#ICFPC-ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

