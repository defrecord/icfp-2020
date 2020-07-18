from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
import sys

# Configure API key authorization: ICFPC-ApiKey
configuration = swagger_client.Configuration()
configuration.host = sys.argv[1]
configuration.api_key['apiKey'] = sys.argv[2]

# create an instance of the API class
api_instance = swagger_client.LogsApiApi(swagger_client.ApiClient(configuration))
log_key = 'log_key_example' # str |

try:
    api_instance.logs_get(log_key)
except ApiException as e:
    print("Exception when calling LogsApiApi->logs_get: %s\n" % e)
