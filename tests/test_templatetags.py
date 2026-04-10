from django.template import Context, Template


def test_templatetag():
    template = """
    {% load display_config_checks run_checks %}
    {% run_unhappy_checks as results_with_failures %}
    {% display_config_checks results_with_failures %}
    """
    rendered = Template(template).render(Context())

    assert "Dummy: Everything is great." in rendered
    assert "Dummy fail: Everything is sad." in rendered
