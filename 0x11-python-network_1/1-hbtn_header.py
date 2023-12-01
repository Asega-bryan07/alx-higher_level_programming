#!/usr/bin/python3
'''
a Python script that takes in a URL, sends a request to the URL and 
displays the value of the X-Request-Id variable found in the header of the response.
must use the packages urllib and sys
not allowed to import packages other than urllib and sys
The value of this variable is different for each request
You don’t need to check arguments passed to the script (number or type)
'''

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        print(dict(response.headers).get('X-Request-Id'))
