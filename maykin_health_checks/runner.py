import traceback
from collections.abc import Callable, Iterable

from django.conf import settings
from django.utils.module_loading import import_string
from django.utils.translation import gettext as _

from .checks import ErrorInfo, GenericHealthCheckResult
from .types import HealthCheck, HealthCheckResult


class ImproperlyConfigured(Exception):
    pass


class HealthChecksRunner:
    """Utility class to run health checks."""

    _checks: Iterable[HealthCheck] | None
    _checks_collector: Callable[[], Iterable[HealthCheck]] | None
    _include_success: bool
    """Whether to return only checks that failed or all checks that ran."""

    def __init__(
        self,
        *,
        checks: Iterable[HealthCheck] | None = None,
        checks_collector: Callable[[], Iterable[HealthCheck]] | None = None,
        include_success: bool = False,
    ):
        if not checks and not checks_collector and not settings.HEALTH_CHECKS:
            raise ImproperlyConfigured(
                "You must provide one or more checks, either via the check parameter,"
                " the check_collector or in the settings.HEALTH_CHECKS."
            )

        self._checks = checks
        self._checks_collector = checks_collector
        self._include_success = include_success

    def get_checks(self) -> Iterable[HealthCheck]:
        if self._checks:
            return self._checks
        elif self._checks_collector:
            return self._checks_collector()

        checks = []
        for check_class_str in settings.HEALTH_CHECKS:
            check_class = import_string(check_class_str)

            check = check_class()
            checks.append(check)

        return checks

    def run_checks(self) -> Iterable[HealthCheckResult]:
        # Get the checks that are configured to run
        checks = self.get_checks()

        # Run the checks and collect the results
        results = []
        for check in checks:
            try:
                result = check.run()
            except Exception:
                result = GenericHealthCheckResult(
                    identifier=check.identifier,
                    success=False,
                    message=_("Something unexpected went wrong."),
                    extra=ErrorInfo(
                        traceback=traceback.format_exc(),
                    ),
                )
            if not result.success or (result.success and self._include_success):
                results.append(result)

        return results
