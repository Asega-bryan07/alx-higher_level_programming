#!/bin/bash
# Bash script that takes in a URL, sends a GET request to the URL
# and displays the body of the response
# Display only body of a 200 status code response
# You have to use curl
# test script in the sandbox provided, using the web server running on port 5000
curl -sL "$1"
