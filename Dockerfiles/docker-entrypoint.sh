#!/bin/sh
python manage.py makemigrations --settings=sdv.settings.qa
python manage.py migrate --noinput --settings=sdv.settings.qa
python manage.py collectstatic --noinput --settings=sdv.settings.qa
gunicorn sdv.wsgi:application --bind 0.0.0.0:80 --workers 3 --timeout 60