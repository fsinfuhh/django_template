#!/usr/bin/bash

exec node /usr/local/src/{{ cookiecutter.project_slug }}/src/{{ cookiecutter.project_slug }}_gui/dist/server/index.mjs
