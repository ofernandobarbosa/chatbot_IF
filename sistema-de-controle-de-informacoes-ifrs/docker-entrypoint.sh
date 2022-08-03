#!/bin/sh
python manage.py makemigrations 
python manage.py migrate --noinput
python manage.py collectstatic --noinput
gunicorn sdv.wsgi:application --bind 0.0.0.0:80 --workers 3 --timeout 60