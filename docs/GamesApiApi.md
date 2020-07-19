# swagger_client.GamesApiApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**games_game_id_get**](GamesApiApi.md#games_game_id_get) | **GET** /games/{gameId} | 
[**games_get**](GamesApiApi.md#games_get) | **GET** /games | 
[**games_non_rating_get**](GamesApiApi.md#games_non_rating_get) | **GET** /games/non-rating | 
[**games_non_rating_run_post**](GamesApiApi.md#games_non_rating_run_post) | **POST** /games/non-rating/run | 

# **games_game_id_get**
> GameDto games_game_id_get(game_id)



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
api_instance = swagger_client.GamesApiApi(swagger_client.ApiClient(configuration))
game_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    api_response = api_instance.games_game_id_get(game_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamesApiApi->games_game_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game_id** | [**str**](.md)|  | 

### Return type

[**GameDto**](GameDto.md)

### Authorization

[ICFPC-ApiKey](../README.md#ICFPC-ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **games_get**
> GamesListDto games_get(tournament_id, take=take, before=before)



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
api_instance = swagger_client.GamesApiApi(swagger_client.ApiClient(configuration))
tournament_id = 56 # int | 
take = 100 # int |  (optional) (default to 100)
before = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

try:
    api_response = api_instance.games_get(tournament_id, take=take, before=before)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamesApiApi->games_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tournament_id** | **int**|  | 
 **take** | **int**|  | [optional] [default to 100]
 **before** | **datetime**|  | [optional] 

### Return type

[**GamesListDto**](GamesListDto.md)

### Authorization

[ICFPC-ApiKey](../README.md#ICFPC-ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **games_non_rating_get**
> GamesListDto games_non_rating_get(take=take, before=before)



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
api_instance = swagger_client.GamesApiApi(swagger_client.ApiClient(configuration))
take = 100 # int |  (optional) (default to 100)
before = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

try:
    api_response = api_instance.games_non_rating_get(take=take, before=before)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamesApiApi->games_non_rating_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **take** | **int**|  | [optional] [default to 100]
 **before** | **datetime**|  | [optional] 

### Return type

[**GamesListDto**](GamesListDto.md)

### Authorization

[ICFPC-ApiKey](../README.md#ICFPC-ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **games_non_rating_run_post**
> games_non_rating_run_post(attacker_submission_id, defender_submission_id)



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
api_instance = swagger_client.GamesApiApi(swagger_client.ApiClient(configuration))
attacker_submission_id = 56 # int | 
defender_submission_id = 56 # int | 

try:
    api_instance.games_non_rating_run_post(attacker_submission_id, defender_submission_id)
except ApiException as e:
    print("Exception when calling GamesApiApi->games_non_rating_run_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attacker_submission_id** | **int**|  | 
 **defender_submission_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[ICFPC-ApiKey](../README.md#ICFPC-ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

