#!/usr/bin/python3
'''
Python script that fetches https://alx-intranet.hbtn.io/status

You must use the package requests
You are not allow to import packages other than requests
'''
import requests

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    r = requests.get(url)
    print('Page Response:')
    print('\t- type {}'.format(type(r.text)))
    print('\t- content {}'.format(r.text))
