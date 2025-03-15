#!/bin/bash
# Send a GET request to the URL and display the body if the status code is 200
[ "$(curl -s -w "%{http_code}" -o response.txt "$1")" -eq 200 ] && cat response.txt
