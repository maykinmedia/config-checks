from maykin_health_checks.checks import ErrorInfo, GenericHealthCheckResult
from maykin_health_checks.runner import HealthChecksRunner
from testapp.checks import CheckWithException, DummyCheck


def test_runner_with_checks_collector():
    runner = HealthChecksRunner(
        checks_collector=lambda: [DummyCheck()], include_success=False
    )
    results = runner.run_checks()

    assert len(list(results)) == 0


def test_runner_include_success():
    runner = HealthChecksRunner(
        checks_collector=lambda: [DummyCheck()], include_success=True
    )
    results = list(runner.run_checks())

    assert len(results) == 1
    assert results[0].success


def test_runner_with_unexpected_exception():
    runner = HealthChecksRunner(
        checks_collector=lambda: [CheckWithException()], include_success=False
    )
    results = list(runner.run_checks())

    assert len(results) == 1

    result = results[0]

    assert isinstance(result, GenericHealthCheckResult)
    assert not result.success
    assert hasattr(result, "extra") and isinstance(result.extra, ErrorInfo)
    assert "HELLO EXCEPTION" in result.extra.traceback
