# naamataulu-backend

## Setting up the environment

### Virtualenv
You need to setup virtualenv to make sure you are using right package versions:

```bash
# Linux
pip install virtualenv                      
virtualenv ENV --python=/usr/bin/python3.6      # We are using Python 3.6
source ENV/bin/activate                         # Activate environment
```

### Using Heroku local

Before running the backend locally make sure you have Heroku CLI installed and
you have the required environment variables in `.env` file.
Template file can be found `template.env`.

```bash
DJANGO_SECRET_KEY=          # https://docs.djangoproject.com/en/2.1/ref/settings/#s-secret-key
DJANGO_DEBUG=True           # https://docs.djangoproject.com/en/2.1/ref/settings/#s-debug
DJANGO_SQLITE=              # True if you want to run local sqlite database
DATABASE_URL=               # Address and credentials of postgres database (Found in Heroku settings)
DISABLE_COLLECTSTATIC=      # Set true for local
WEB_CONCURRENCY=            # How many instances of the backend Gunicorn runs (1 is enough for local testing)
```

```bash
source ENV/bin/activate

# Run one of these:

# Install dependencies and run migrations
# (Needs to be ran after dependency or database changes)
heroku local release -f Procfile.linux 

# manage.py makemigrations (generate migration files after changing the model)
heroku local makemigrations -f Procfile.linux   

# Run the backend
heroku local web -f Procfile.linux              
```

### Without Heroku

If you don't want to install Heroku you take a peek at Procfiles to determine what you need to run.
After loading environment variables and installing dependencies, the backend should run just fine.

## Modifying the model

If you modify the models (models.py) make sure to create migration files so they can be ran by other developers / production environment!

```bash
heroku local makemigrations -f Procfile.linux
```
