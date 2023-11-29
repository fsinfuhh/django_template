from django.apps import AppConfig


class ApiConfig(AppConfig):
    name = "{{ cookiecutter.project_slug }}.api"
    label = "{{ cookiecutter.project_slug }}_api"
