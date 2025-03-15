#!/bin/bash
# Send a GET request and display the body of the response only if status code is 200
response=$(curl -s -w "%{http_code}" -o response.txt "$1")
if [ "$response" -eq 200 ]; then
    cat response.txt
fi
