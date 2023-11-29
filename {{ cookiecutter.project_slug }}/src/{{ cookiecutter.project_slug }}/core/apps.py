from django.apps import AppConfig


class CoreConfig(AppConfig):
    name = "{{ cookiecutter.project_slug }}.core"
    label = "{{ cookiecutter.project_slug }}_core"
