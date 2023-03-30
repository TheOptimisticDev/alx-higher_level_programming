#!/bin/bash
# This scripts sends a POST request with a variables
curl -s "$1" -X POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD"

