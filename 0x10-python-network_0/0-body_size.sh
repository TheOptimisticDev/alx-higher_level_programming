#!/bin/bash
# This script is to print the body size of the header
curl -Is "$1" | grep Content-Length | cut -d " " -f 2
