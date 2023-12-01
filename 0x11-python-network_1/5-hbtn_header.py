#!/usr/bin/python3
'''
a Python script that takes in a URL, sends a request to the URL
and displays the value of the variable X-Request-Id in the response header
must use the packages requests and sys
not allowed to import other packages than requests and sys
The value of this variable is different for each request
'''

import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]

    r = requests.get(url)
    print(r.headers.get('X-Request-Id'))
