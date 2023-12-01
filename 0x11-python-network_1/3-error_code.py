#!/usr/bin/python3
'''
Python script that takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8).
You have to manage urllib.error.HTTPError exceptions and print:
Error code: followed by the HTTP status code
You must use the packages urllib and sys
You are not allowed to import other packages than urllib and sys
You don’t need to check arguments passed to the script (number or type)
'''
import sys
import urllib.request
import urllib.error

if __name__ == "__main__":
    url = sys.argv[1]

    req = urllib.request.Request(url)

    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode('ascii'))
    except urllib.error.HTTPError as e:
        print('Error code: {}'.format(e.code))
