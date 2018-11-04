#!/bin/sh
export $(cat .env | xargs)
cd src/naamataulu
python manage.py runserver
