from collections.abc import Callable, Iterable

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, JsonResponse
from django.views import View

from ..runner import HealthChecksRunner
from ..types import HealthCheck


class HealthChecksView(LoginRequiredMixin, View):
    raise_exception: bool = True
    checks_collector: Callable[[], Iterable[HealthCheck]] = lambda: []
    """
    The method to gather the HealthChecks that the view will run.

    Specify this as an initkwargs in the ``as_view(checks_collector=...)`` class method.
    """

    def get(self, request: HttpRequest, *args, **kwargs) -> JsonResponse:
        include_success = request.GET.get("include_success") == "yes"

        runner = HealthChecksRunner(
            checks_collector=self.checks_collector,
            include_success=include_success,
        )
        results = runner.run_checks()

        return JsonResponse([result.to_builtins() for result in results], safe=False)
