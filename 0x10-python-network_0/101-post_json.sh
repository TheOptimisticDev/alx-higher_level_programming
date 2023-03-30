#!/bin/bash
# This script sends a POST request with a json file
curl -s "$1" -X "POST" -H "Content-Type: application/json" -d "@$2"
