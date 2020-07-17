from __future__ import print_function
from pprint import pprint
from swagger_client.rest import ApiException
import requests
import sys
import time
import swagger_client

def main():
    server_url = f"{sys.argv[1]}/aliens/send?apiKey={sys.argv[2]}"
    data = "01"
    print('ServerUrl: %s; Data: %s' % (server_url, data))

    res = requests.post(server_url, data=data)
    print(res)
    if res.status_code != 200:
        print('Unexpected server response:')
        print('HTTP code:', res.status_code)
        print('Response body:', res.text)
        exit(2)
    print('Server response:', res.text)


if __name__ == '__main__':
    main()
