#!/bin/sh
docker-compose run web bash -c "cd src/naamataulu && python3 manage.py test api/tests"