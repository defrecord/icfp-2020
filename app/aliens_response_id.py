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
api_instance = swagger_client.AliensApiApi(swagger_client.ApiClient(configuration))
response_id = '1' # str |

try:
    api_instance.aliens_response_id_get(response_id)
except ApiException as e:
    print("Exception when calling AliensApiApi->aliens_response_id_get: %s\n" % e)
