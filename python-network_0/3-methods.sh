#!/bin/bash
# Get the allowed HTTP methods for the given URL
curl -s -I "$1" | grep "Allow" | cut -d " " -f2-
