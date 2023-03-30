#!/bin/bash
# This script prints the status code of the server
curl -so /dev/null -w "%{http_code}" "$1"
