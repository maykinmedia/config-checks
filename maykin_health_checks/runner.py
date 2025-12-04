import traceback
from collections.abc import Callable, Iterable

from django.utils.translation import gettext as _

from .checks import ErrorInfo, GenericHealthCheckResult
from .types import HealthCheck, HealthCheckResult


class ImproperlyConfigured(Exception):
    pass


class HealthChecksRunner:
    """Utility class to run health checks."""

    _checks_collector: Callable[[], Iterable[HealthCheck]]
    _include_success: bool
    """Whether to return only checks that failed or all checks that ran."""

    def __init__(
        self,
        *,
        checks_collector: Callable[[], Iterable[HealthCheck]],
        include_success: bool = True,
    ):
        self._checks_collector = checks_collector
        self._include_success = include_success

    def run_checks(self) -> Iterable[HealthCheckResult]:
        checks = self._checks_collector()

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
