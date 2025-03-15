#!/bin/bash
# Send a GET request to the URL, follow redirects, and display the body of the response if the status code is 200
curl -s -L "$1"
