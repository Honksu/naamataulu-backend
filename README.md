# naamataulu-backend

## Setting up the environment

Create file:

```src/naamataulu/naamataulu/secret_settings.py```

with contents

```SECRET_KEY='*some secret key*'```

Install requirements

Django first time setup

pip3 and python3 might be just pip and python depending on your environment.
*TODO Virtualenv/Docker*

```bash
pip3 install -r src/requirements.txt
cd src/naamataulu
python3 manage.py makemigrations
python3 manage.py createsuperuser
python3 manage.py runserver
```

## Modifying the model

If you modify the models (models.py) make sure to create migration files so they can be ran by other developers / production environment!

```bash
# Creates the migration script to migrations directory
python3 manage.py migrate

# Runs the migrations on local database
python3 manage.py makemigrations
```