#! /bin/bash

python manage.py migrate default

if [ "$1" = 'run_bot' ]; then
    exec python manage.py main
fi

python manage.py collectstatic --no-input

exec gunicorn bot_backend.wsgi:application -b 0.0.0.0:8000 --reload