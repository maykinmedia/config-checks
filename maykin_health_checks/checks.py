from dataclasses import asdict, dataclass

from maykin_health_checks.types import JSONValue


@dataclass
class ErrorInfo:
    traceback: str


@dataclass
class GenericHealthCheckResult:
    success: bool
    identifier: str
    """Identifier needed to clarify from which health check this result comes from."""
    message: str
    extra: ErrorInfo | None = None

    def to_builtins(self) -> JSONValue:
        return asdict(self)
