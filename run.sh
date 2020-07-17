#!/bin/sh

echo python app/main.py server_url api_key
python app/main.py "$@" || echo "run error code: $?"
