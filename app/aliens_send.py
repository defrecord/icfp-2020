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
body = '1101000' # str |  (optional)

try:
    res = api_instance.aliens_send_post(body=body)
    pprint(res)
    # https://github.com/icfpcontest2020/aliens-proxy-protocol
    print('1101100001110111110111101010101011100')
except ApiException as e:
    print("Exception when calling AliensApiApi->aliens_send_post: %s\n" % e)
