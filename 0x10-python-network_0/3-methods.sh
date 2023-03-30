#!/bin/bash
# This script displays the HTTP methods allowed by the server
curl -sI "$1" -X OPTIONS | grep -oP "(?<=(^Allow:\s))(\w.*)$"

