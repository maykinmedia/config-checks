from typing import Protocol

JSONValue = dict[str, "JSONValue"] | list["JSONValue"] | str | int | float | bool | None

type Slug = str


class HealthCheckResult[T](Protocol):
    success: bool
    identifier: Slug
    message: str = ""
    extra: T
    """Attribute to include additional info in the health check result."""

    def to_builtins(self) -> JSONValue:
        """Return a serialisable object."""
        ...


class HealthCheck[T](Protocol):
    identifier: Slug
    "Used as the HealthCheckResult.identifier for uncaught exceptions"

    def run(self) -> HealthCheckResult[T]: ...
