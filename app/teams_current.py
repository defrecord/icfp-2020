from __future__ import print_function
from pprint import pprint
from swagger_client.rest import ApiException
import requests
import sys
import time
import swagger_client
import json

def main():
    configuration = swagger_client.Configuration()
    configuration.host = sys.argv[1]
    configuration.api_key['apiKey'] = sys.argv[2]
    api_instance = swagger_client.TeamsApiApi(swagger_client.ApiClient(configuration))


    try:
        api_response = api_instance.teams_current_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TeamsApiApi->teams_current_get: %s\n" % e)

if __name__ == '__main__':
    main()
