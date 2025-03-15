#!/bin/bash
response=$(curl -s -w "%{http_code}" -o response.txt "$1")
[ "$response" -eq 200 ] && cat response.txt
