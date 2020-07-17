from __future__ import print_function
from pprint import pprint
from swagger_client.rest import ApiException
import requests
import sys
import time
import swagger_client

def main():
    path = "aliens/send"
    server_url = f"{sys.argv[1]}/{path}?apiKey={sys.argv[2]}"
    data = "01"

    # requests
    print('ServerUrl: %s; Data: %s' % (server_url, data))
    res = requests.post(server_url, data=data)
    print(res)
    if res.status_code != 200:
        print('Unexpected server response:')
        print('HTTP code:', res.status_code)
        print('Response body:', res.text)
        exit(2)
    print('Server response:', res.text)

    # swagger
    # Configure API key authorization: ICFPC-ApiKey
    configuration = swagger_client.Configuration()
    configuration.host = sys.argv[1]
    configuration.api_key['apiKey'] = sys.argv[2]
    api_instance = swagger_client.AliensApiApi(swagger_client.ApiClient(configuration))
    body = data

    try:
        api_instance.aliens_send_post(body=body)
    except ApiException as e:
        print("Exception when calling AliensApiApi->aliens_send_post: %s\n" % e)




if __name__ == '__main__':
    main()
