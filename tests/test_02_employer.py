from http import HTTPStatus

import pytest

from .utils import employer_utils as utils


@pytest.mark.django_db()
class Test02Employer:
    url = "/api/v1/employers/me/"

    @pytest.mark.parametrize("data,messege", utils.EMPLOYER_EDIT_VALID_DATA)
    def test_01_employer_update_success(self, employer_client, data, messege):
        """Удачное изменение профиля работодателя."""
        response = employer_client.patch(self.url, data=data)
        assert response.status_code == HTTPStatus.OK, (
            f"Запрос на изменение профиля с валидными данными({messege})"
            f" возвращает статус {response.status_code}."
        )
        for key, val in data.items():
            assert (
                response.data[key] == val
            ), f'Изменение профиля компании по полю "{key}" прошло неверно.'

    @pytest.mark.parametrize("data,messege", utils.EMPLOYER_EDIT_INVALID_DATA)
    def test_02_create_employer_fail(self, employer_client, data, messege):
        """Изменение профиля работодателя с невалидными данными."""
        response = employer_client.patch(self.url, data=data)
        assert response.status_code == HTTPStatus.BAD_REQUEST, (
            "Запрос на изменение профиля с невалидными данными "
            f"({messege}) возвращает статус {response.status_code}."
        )

    def test_03_access_to_url(self, employer_client, guest_client):
        """Личный кабинет работодателя доступен только этой роли."""
        expectation = (
            ("гость", guest_client, HTTPStatus.UNAUTHORIZED),
            ("компания", employer_client, HTTPStatus.OK),
        )
        for name, client, code in expectation:
            response = client.get(self.url)
            assert response.status_code == code, (
                f'При GET-запросе на {self.url} от клиента "{name}"'
                f"пришел статус {response.status_code}"
            )
