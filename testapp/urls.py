from django.contrib import admin
from django.urls import path

from maykin_config_checks.api.views import ConfigChecksView
from testapp.checks import DummyCheck, DummyCheckFail

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "config-checks",
        ConfigChecksView.as_view(
            checks_collector=lambda: [DummyCheck(), DummyCheckFail()]
        ),
        name="config-checks",
    ),
]
