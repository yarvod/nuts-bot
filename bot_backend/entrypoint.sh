#! /bin/bash

python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --no-input

if [ "$1" = 'run_bot' ]; then
  exec python manage.py main
fi

if [ "$1" = 'run_django' ]; then
  exec gunicorn bot_backend.wsgi:application -b 0.0.0.0:8000 --reload
fi