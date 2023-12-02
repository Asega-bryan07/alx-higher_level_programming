#!/bin/bash
# Bash script that makes a request to 0.0.0.0:5000/catch_me
# that causes the server to respond with a message containing 
# You got me! in the body of the response.
# You have to use curl
# You are not allow to use echo, cat, etc. to display the final result
# test your script in the sandbox provided, using the web server
# running on port 5000
curl -sL -X PUT -H "Origin: ALXSoftwareEngineering" -d "user_id=98 0.0.0.0:5000/catch_me" "$1"
