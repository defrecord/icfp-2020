from __future__ import print_function
from pprint import pprint
from swagger_client.rest import ApiException
from pprint import pprint
import requests
import sys
import time
import swagger_client

def main():
    # Configure API key authorization: ICFPC-ApiKey
    configuration = swagger_client.Configuration()
    configuration.host = sys.argv[1]
    configuration.api_key['apiKey'] = sys.argv[2]


    # create an instance of the API class
    api_instance = swagger_client.AliensApiApi(swagger_client.ApiClient(configuration))
    body = '01' # str |  (optional)

    # try:
    #     res = api_instance.aliens_send_post(body=body)
    #     pprint(res)
    # except ApiException as e:
    #     print("Exception when calling AliensApiApi->aliens_send_post: %s\n" % e)


    path = "aliens/send"
    server_url = f"{sys.argv[1]}/{path}?apiKey={sys.argv[2]}"
    print(f"{sys.argv[1]} {sys.argv[2]}")
    data = "1101000"

    # requests
    print('ServerUrl: %s; Data: %s' % (server_url, data))
    res = requests.post(server_url, data=data)
    print(res)
    # https://github.com/icfpcontest2020/aliens-proxy-protocol
    if res.status_code == 302:
        print('Response body:', res.text)

    if res.status_code != 200:
        print('Unexpected server response:')
        print('HTTP code:', res.status_code)
        print('Response body:', res.text)
        exit(2)
    print('Server response:', res.text)
    # https://github.com/icfpcontest2020/aliens-proxy-protocol
    print('Server expected:', '1101100001110111110111101010101011100')


if __name__ == '__main__':
    main()
