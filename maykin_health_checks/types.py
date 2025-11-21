from typing import Protocol

JSONValue = dict[str, "JSONValue"] | list["JSONValue"] | str | int | float | bool | None


class HealthCheckResult[T](Protocol):
    success: bool
    identifier: str
    message: str = ""
    extra: T
    """Attribute to include additional info in the health check result."""

    def to_builtins(self) -> JSONValue:
        """Return a serialisable object."""
        ...


class HealthCheck[T](Protocol):
    identifier: str

    def run(self) -> HealthCheckResult[T]: ...
