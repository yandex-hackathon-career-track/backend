import pytest

from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import AccessToken

from apps.users.services import create_user_with_profile


@pytest.fixture
def employer_user(django_user_model):
    data = {"email": "employer@unexisting_mail.ru", "password": "TestPass-123"}
    user = create_user_with_profile(data)
    return user


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
def employer2_user(django_user_model):
    data = {"email": "employer2@unexisting.ru", "password": "TestPass-123"}
    user = create_user_with_profile(data)
    return user


@pytest.fixture
def employer2_token(employer2_user):
    token = AccessToken.for_user(employer2_user)
    return {"access": str(token)}


@pytest.fixture
def employer2_client(employer2_token):
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION=f'JWT {employer2_token["access"]}')
    return client


@pytest.fixture
def guest_client():
    return APIClient()
