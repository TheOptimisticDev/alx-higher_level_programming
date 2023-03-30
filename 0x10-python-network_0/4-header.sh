#!/bin/bash
# This script sends a GET with variable X-Holberton-User-Id equals 98
curl -s "$1" -H "X-HolbertonSchool-User-Id: 98"
