# swagger_client.SubmissionsApiApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**submissions_get**](SubmissionsApiApi.md#submissions_get) | **GET** /submissions | 
[**submissions_other_teams_get**](SubmissionsApiApi.md#submissions_other_teams_get) | **GET** /submissions/other-teams | 
[**submissions_submission_id_activate_post**](SubmissionsApiApi.md#submissions_submission_id_activate_post) | **POST** /submissions/{submissionId}/activate | 
[**submissions_submission_id_get**](SubmissionsApiApi.md#submissions_submission_id_get) | **GET** /submissions/{submissionId} | 

# **submissions_get**
> list[SubmissionDto] submissions_get()



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
api_instance = swagger_client.SubmissionsApiApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.submissions_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubmissionsApiApi->submissions_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[SubmissionDto]**](SubmissionDto.md)

### Authorization

[ICFPC-ApiKey](../README.md#ICFPC-ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submissions_other_teams_get**
> list[TeamSubmissionDto] submissions_other_teams_get(tournament_id)



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
api_instance = swagger_client.SubmissionsApiApi(swagger_client.ApiClient(configuration))
tournament_id = 56 # int | 

try:
    api_response = api_instance.submissions_other_teams_get(tournament_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubmissionsApiApi->submissions_other_teams_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tournament_id** | **int**|  | 

### Return type

[**list[TeamSubmissionDto]**](TeamSubmissionDto.md)

### Authorization

[ICFPC-ApiKey](../README.md#ICFPC-ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submissions_submission_id_activate_post**
> submissions_submission_id_activate_post(submission_id)



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
api_instance = swagger_client.SubmissionsApiApi(swagger_client.ApiClient(configuration))
submission_id = 56 # int | 

try:
    api_instance.submissions_submission_id_activate_post(submission_id)
except ApiException as e:
    print("Exception when calling SubmissionsApiApi->submissions_submission_id_activate_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **submission_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[ICFPC-ApiKey](../README.md#ICFPC-ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submissions_submission_id_get**
> SubmissionDto submissions_submission_id_get(submission_id)



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
api_instance = swagger_client.SubmissionsApiApi(swagger_client.ApiClient(configuration))
submission_id = 56 # int | 

try:
    api_response = api_instance.submissions_submission_id_get(submission_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubmissionsApiApi->submissions_submission_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **submission_id** | **int**|  | 

### Return type

[**SubmissionDto**](SubmissionDto.md)

### Authorization

[ICFPC-ApiKey](../README.md#ICFPC-ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

