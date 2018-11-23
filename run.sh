#!/bin/sh
export $(cat .env | xargs)
cd src/naamataulu
if [ -z "$1" ]
  then
    python manage.py runserver
  else
    python manage.py "$@"
fi
