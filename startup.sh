#!/bin/bash
python /app/main.py &
cd /html
pwd
python -m http.server 8080