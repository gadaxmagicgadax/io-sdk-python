#!/bin/bash
cd "$(dirname $0)"

echo "preparing archive, please wait..."
zip -qr index.zip __main__.py config.py

wsk action update iosdk/import index.zip --kind python:3 --web true
 
