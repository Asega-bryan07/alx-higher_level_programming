#!/bin/bash
# Bash script that sends a request to a URL passed as an argument, and 
# displays only the status code of the response.
# You are not allowed to use any pipe, redirection, etc.
# You are not allowed to use ; and &&
# You have to use curl
curl -s -o /dev/null -w "%{http_code}" "$1"
