import pytest

from apps.attributes.models import City, Occupation, WorkFormat


@pytest.fixture
def city():
    return City.objects.create(name="СПб")


@pytest.fixture
def full_occupation():
    return Occupation.objects.create(name="Полная")


@pytest.fixture
def remote_format():
    return WorkFormat.objects.create(name="Удаленка")
