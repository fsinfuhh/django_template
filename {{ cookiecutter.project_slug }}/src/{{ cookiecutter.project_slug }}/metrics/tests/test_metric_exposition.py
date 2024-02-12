from django.shortcuts import resolve_url
from django.test import Client


def test_metric_endpoint_returns_200(client: Client):
    response = client.get(resolve_url("prometheus_metrics"))
    assert response.status_code == 200
