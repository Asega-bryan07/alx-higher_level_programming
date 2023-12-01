#!/usr/bin/python3
'''
Python script that takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter, and displays the body
of the response (decoded in utf-8)
The email must be sent in the email variable
You must use the packages urllib and sys
You are not allowed to import packages other than urllib and sys
You don’t need to check arguments passed to the script (number or type)
'''
import urllib.request
import urllib.parse
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    value = {"email": argv[2]}
    v_decode = urllib.parse.urlencode(value).encode('ascii')  '''in bytes'''

    req = urllib.request.Request(url, data=v_decode)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
