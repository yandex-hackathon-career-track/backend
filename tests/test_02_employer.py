from http import HTTPStatus

import pytest

from . import utils


@pytest.mark.django_db()
class Test02Employer:
    create_url = "/api/v1/users/"

    @pytest.mark.parametrize("data,messege", utils.EMPLOYER_CREATE_VALID_DATA)
    def test_01_create_employer_success(self, guest_client, data, messege):
        """Создание пользователя с валидными данными."""
        response = guest_client.post(self.create_url, data=data)
        assert response.status_code == HTTPStatus.CREATED, (
            f"POST-Запрос на создание компании с валидными данными({messege})"
            f" возвращает статус {response.status_code}."
        )

    @pytest.mark.parametrize(
        "data,messege", utils.EMPLOYER_CREATE_INVALID_DATA
    )
    def test_02_create_employer_fail(self, guest_client, data, messege):
        """Создание пользователя с невалидными данными."""
        response = guest_client.post(self.create_url, data=data)
        assert response.status_code == HTTPStatus.BAD_REQUEST, (
            "POST-Запрос на создание компании с невалидными данными "
            f"({messege}) возвращает статус {response.status_code}."
        )
