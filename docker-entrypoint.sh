#!/bin/bash
cd src/naamataulu

python3 manage.py collectstatic --noinput

echo "Starting Gunicorn"
exec gunicorn naamataulu.wsgi
    --preload
    --bind 0.0.0.0:$PORT