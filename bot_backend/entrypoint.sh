#! /bin/bash

if [ "$1" = "run_django" ]; then
  python manage.py migrate
  python manage.py collectstatic --no-input
  exec gunicorn bot_backend.wsgi:application -b 0.0.0.0:8000 --reload
fi

if [ "$1" = 'run_bot' ]; then
  python manage.py migrate
  exec python manage.py main
fi