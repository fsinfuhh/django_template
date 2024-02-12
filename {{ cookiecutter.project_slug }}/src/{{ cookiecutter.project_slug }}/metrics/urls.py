from django.urls import path

from {{ cookiecutter.project_slug }}.metrics import views

urlpatterns = [
    path("", views.PrometheusMetricsView.as_view(), name="prometheus_metrics"),
]
