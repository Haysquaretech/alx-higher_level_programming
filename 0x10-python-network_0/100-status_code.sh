#!/bin/bash
# send a request to a URL, and also displays only the status code of the response.
curl -s -o /dev/null -w "%{http_code}" "$1"
