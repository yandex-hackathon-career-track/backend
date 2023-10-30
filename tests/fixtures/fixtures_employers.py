import pytest

from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import AccessToken

from apps.users.services import create_user_with_profile


@pytest.fixture
def employer_user(django_user_model):
    data = {"email": "employer@unexisting_mail.ru", "password": "TestPass-123"}
    return create_user_with_profile(data)


@pytest.fixture
def employer_token(employer_user):
    token = AccessToken.for_user(employer_user)
    return {"access": str(token)}


@pytest.fixture
def employer_client(employer_token):
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION=f'JWT {employer_token["access"]}')
    return client


@pytest.fixture
def guest_client():
    return APIClient()
