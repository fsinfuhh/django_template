#!/usr/bin/bash
set -e

D=/usr/local/src/{{ cookiecutter.project_slug }}/src/
$D/manage.py migrate
$D/manage.py collectstatic --noinput
$D/manage.py check --deploy

exec gunicorn \
  --workers=$(nproc --all) \
  --pythonpath /usr/local/src/{{ cookiecutter.project_slug }}/src/ \
  {{ cookiecutter.project_slug }}.wsgi:application
