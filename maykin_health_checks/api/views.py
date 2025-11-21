from collections.abc import Callable, Iterable

from django.http import HttpRequest, JsonResponse
from django.views import View

from ..runner import HealthChecksRunner
from ..types import HealthCheck


class HealthChecksView(View):
    checks_collector: Callable[[], Iterable[HealthCheck]] | None = None
    checks: Iterable[HealthCheck] | None = None

    def get(self, request: HttpRequest, *args, **kwargs) -> JsonResponse:
        include_sucess = request.GET.get("include_success") == "yes"

        runner = HealthChecksRunner(
            checks=self.checks,
            checks_collector=self.checks_collector,
            include_success=include_sucess,
        )
        results = runner.run_checks()

        return JsonResponse([result.to_builtins() for result in results], safe=False)
