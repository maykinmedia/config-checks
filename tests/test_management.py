from io import StringIO

from django.core.management import call_command


def test_management_command():
    out = StringIO()
    call_command(
        "health_checks", checks_collector="testapp.checks.check_collector", stdout=out
    )

    assert (
        "Error dummy_fail: Everything is sad.\n{'info': 'bla'}"
        == out.getvalue().strip("\n")
    )


def test_management_command_with_success():
    out = StringIO()

    call_command(
        "health_checks",
        checks_collector="testapp.checks.check_collector",
        include_success=True,
        stdout=out,
    )

    assert (
        "Correctly configured: dummy\n"
        "Error dummy_fail: Everything is sad.\n{'info': 'bla'}\n" == out.getvalue()
    )
