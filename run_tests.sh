#!/bin/sh
export $(cat .env | xargs)
cd src/naamataulu
python manage.py test api/tests