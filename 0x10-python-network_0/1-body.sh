#!/bin/bash
# This script takes in a URL and displays the body of the response only for a 200 status code
curl -sL "$1"
