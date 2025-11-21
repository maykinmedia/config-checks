from msgspec import UNSET, Struct, UnsetType, to_builtins

from maykin_health_checks.types import JSONValue


class ErrorInfo(Struct):
    traceback: str


class GenericHealthCheckResult(Struct):
    success: bool
    identifier: str
    """Identifier needed to clarify from which health check this result comes from."""
    message: str
    extra: ErrorInfo | UnsetType = UNSET

    def to_builtins(self) -> JSONValue:
        return to_builtins(self)
