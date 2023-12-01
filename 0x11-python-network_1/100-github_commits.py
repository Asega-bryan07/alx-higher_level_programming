#!/usr/bin/python3

'''
Holberton School staff evaluates candidates applying for a back-end position with 
multiple technical challenges, like this one:

    Please list 10 commits (from the most recent to oldest) of the repository
    “rails” by the user “rails”

    You must use the GitHub API, here is the documentation:
    https://developer.github.com/v3/repos/commits/
    Print all commits by: `<sha>: <author name>` (one by line)
    Write a Python script that takes 2 arguments in order to solve this challenge.

    The first argument will be the repository name
    The second argument will be the owner name
    You must use the packages requests and sys
    You are not allowed to import packages other than requests and sys
    You don’t need to check arguments passed to the script (number or type)
    Only 17% of applicants for a backend position at Holberton finished this task in less
    than 15 minutes.

LETS DO IT!
'''
from sys import argv
import requests

if __name__ == "__main__":
    url = 'https://developer.github.com/v3/repos/{}/{}/commits/'.format(
            argv[2], argv[1])

    r = requests.get(url)
    commits = r.json()

    try:
        for i in range(10):
            print('{}: {}'.format(
                commits[i].get('sha'),
                commits[i].get('commit').get('author').get('name')))
    except IndexError:
        pass
