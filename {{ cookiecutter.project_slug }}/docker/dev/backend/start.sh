#!/bin/bash

ln -sf /app/config/.env.dev.local /app/backend/.env.dev.local

pipenv install --dev --system --ignore-pipfile

python3 src/manage.py migrate
python3 src/manage.py runserver 0.0.0.0:8000
