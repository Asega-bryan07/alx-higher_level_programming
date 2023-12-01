#!/usr/bin/python3
'''
Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
must use Basic Authentication with a personal access token as password to
access to your information (only read:user permission is needed)

The first argument will be your username
The second argument will be your password (in your case, a personal access token as password)
must use the package requests and sys
not allowed to import packages other than requests and sys
no need to check arguments passed to the script (number or type)
'''

import requests
from sys import argv
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    auth = HTTPBasicAuth(argv[1], argv[2])

    r = requests.get('https://api.github.com/user', auth=auth)
    print(r.json().get('id'))
