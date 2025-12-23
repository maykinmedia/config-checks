from django.contrib import admin
from django.urls import path

from maykin_config_checks.api.views import HealthChecksView
from testapp.checks import DummyCheck, DummyCheckFail

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "health-checks",
        HealthChecksView.as_view(
            checks_collector=lambda: [DummyCheck(), DummyCheckFail()]
        ),
        name="health-checks",
    ),
]
