from collections.abc import Iterable
from dataclasses import asdict, dataclass

from maykin_health_checks.types import HealthCheck, HealthCheckResult, JSONValue


@dataclass
class DummyResult:
    success: bool
    identifier: str
    message: str = ""
    extra: dict | None = None

    def to_builtins(self) -> JSONValue:
        return asdict(self)


class DummyCheck:
    identifier = "dummy"

    def run(self) -> HealthCheckResult:
        return DummyResult(
            success=True, identifier=self.identifier, message="Everything is great."
        )


class DummyCheckFail:
    identifier = "dummy_fail"

    def run(self) -> HealthCheckResult:
        return DummyResult(
            success=False,
            identifier=self.identifier,
            message="Everything is sad.",
            extra={"info": "bla"},
        )


class CheckWithException:
    identifier = "check_with_exception"

    def run(self) -> HealthCheckResult:
        raise Exception("HELLO EXCEPTION!")


def check_collector() -> Iterable[HealthCheck]:
    return [DummyCheck(), DummyCheckFail()]
