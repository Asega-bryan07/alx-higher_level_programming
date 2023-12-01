#!/usr/bin/python3
'''
a Python script that fetches https://alx-intranet.hbtn.io/status

You must use the package urllib
You are not allowed to import any packages other than urllib
The body of the response must be displayed like the following example (tabulation before -)
must use a with statement
'''
import urllib

with urllib.requests.open('https://alx-intranet.hbtn.io/status') as response:
    html = response.read()
