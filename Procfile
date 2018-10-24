release: cd src/naamataulu && python manage.py migrate
web: cd src/naamataulu && gunicorn naamataulu.wsgi --preload -b 0.0.0.0:$PORT