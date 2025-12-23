from collections.abc import Iterable
from dataclasses import asdict, dataclass

from maykin_health_checks import HealthCheck, HealthCheckResult, JSONValue


@dataclass
class DummyResult:
    success: bool
    identifier: str
    verbose_name: str
    message: str = ""
    extra: dict | None = None

    def to_builtins(self) -> JSONValue:
        return asdict(self)


class DummyCheck:
    identifier = "dummy"
    verbose_name = "Dummy"

    def __call__(self) -> HealthCheckResult:
        return DummyResult(
            success=True,
            verbose_name=self.verbose_name,
            identifier=self.identifier,
            message="Everything is great.",
        )


class DummyCheckFail:
    identifier = "dummy_fail"
    verbose_name = "Dummy fail"

    def __call__(self) -> HealthCheckResult:
        return DummyResult(
            success=False,
            verbose_name=self.verbose_name,
            identifier=self.identifier,
            message="Everything is sad.",
            extra={"info": "bla"},
        )


class CheckWithException:
    identifier = "check_with_exception"
    verbose_name = "Check with exception"

    def __call__(self) -> HealthCheckResult:
        raise Exception("HELLO EXCEPTION!")


def check_collector() -> Iterable[HealthCheck]:
    return [DummyCheck(), DummyCheckFail()]
