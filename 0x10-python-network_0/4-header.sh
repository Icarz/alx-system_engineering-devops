#!/bin/bash
# This script sends a GET request with a custom header X-School-User-Id set to 98 and displays the body of the response
curl -sH "X-School-User-Id: 98" "$1"
