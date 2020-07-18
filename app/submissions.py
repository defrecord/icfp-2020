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

api_instance = swagger_client.SubmissionsApiApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.submissions_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubmissionsApiApi->submissions_get: %s\n" % e)
