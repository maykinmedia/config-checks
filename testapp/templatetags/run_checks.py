from django import template

from maykin_config_checks import run_checks

from ..checks import DummyCheck, DummyCheckFail

register = template.Library()


@register.simple_tag
def run_happy_checks():
    return run_checks(
        checks_collector=lambda: [DummyCheck()],
        include_success=True,
    )


@register.simple_tag
def run_unhappy_checks():
    return run_checks(
        checks_collector=lambda: [DummyCheck(), DummyCheckFail()],
        include_success=True,
    )
