#!/bin/bash
# Bash script that sends a DELETE request to the URL passed as
# the first argument and displays the body of the response
# You have to use curl
curl -sX DELETE "$1"
