from django.contrib.auth.models import AbstractUser
from django.test import Client
from django.urls import reverse


def test_not_logged_in(client: Client):
    checks_url = reverse("health-checks-injected-collector")

    response = client.get(checks_url)

    assert response.status_code == 403


def test_view_injected_collector(client: Client, django_user_model: AbstractUser):
    checks_url = reverse(
        "health-checks-injected-collector"
    )  # Uses injected checks collector.
    user = django_user_model.objects.create_user(
        username="johndoe", password="verysecret"
    )
    client.force_login(user)

    response = client.get(checks_url)

    assert response.status_code == 200
    assert response.json() == [
        {"success": False, "identifier": "dummy_fail", "message": "Everything is sad."}
    ]


def test_view_injected_checks(client: Client, django_user_model: AbstractUser):
    checks_url = reverse("health-checks-injected-checks")  # Uses injected checks.
    user = django_user_model.objects.create_user(
        username="johndoe", password="verysecret"
    )
    client.force_login(user)

    response = client.get(checks_url)

    assert response.status_code == 200
    assert response.json() == [
        {"success": False, "identifier": "dummy_fail", "message": "Everything is sad."}
    ]


def test_view_with_success(client: Client, django_user_model: AbstractUser):
    checks_url = reverse(
        "health-checks-injected-collector"
    )  # Uses injected checks collector.
    user = django_user_model.objects.create_user(
        username="johndoe", password="verysecret"
    )
    client.force_login(user)

    # TODO: change when we drop support for Django 4.2
    # response = client.get(checks_url, query_params={"include_success": "yes"})
    response = client.get(f"{checks_url}?include_success=yes")

    assert response.status_code == 200
    assert response.json() == [
        {"success": True, "identifier": "dummy", "message": "Everything is great."},
        {"success": False, "identifier": "dummy_fail", "message": "Everything is sad."},
    ]
