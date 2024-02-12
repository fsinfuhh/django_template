from django.apps import AppConfig
from opentelemetry import metrics
from opentelemetry.exporter.prometheus import PrometheusMetricReader
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.resources import SERVICE_NAME, SERVICE_VERSION, Resource
from {{cookiecutter.project_slug}} import __version__ as app_version


class MetricsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "{{ cookiecutter.project_slug }}.metrics"
    label = "{{ cookiecutter.project_slug }}_metrics"

    def ready(self):
        super().ready()
        self.init_instrumentation()

    def init_instrumentation(self):
        from {{ cookiecutter.project_slug }}.metrics import async_instruments

        resource = Resource(
            attributes={
                SERVICE_NAME: "{{ cookiecutter.project_slug }}",
                SERVICE_VERSION: app_version,
            }
        )
        metric_reader = PrometheusMetricReader()
        meter_provider = MeterProvider(resource=resource, metric_readers=[metric_reader])
        metrics.set_meter_provider(meter_provider)
        async_instruments.create_async_instruments()
