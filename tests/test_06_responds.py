from http import HTTPStatus

import pytest


@pytest.mark.django_db()
class Test06Responds:
    list_url = "/api/v1/employers/vacancies/{id}/responds/"

    def test_01_access_to_url(self, employer_client, guest_client, vacancy):
        """Разделы 'Отклики' доступны только компании-автору вакансии."""
        url = self.list_url.format(id=vacancy.id)
        expectation = (
            ("гость", guest_client, HTTPStatus.UNAUTHORIZED),
            ("компания", employer_client, HTTPStatus.OK),
        )
        for name, client, code in expectation:
            response = client.get(url)
            assert response.status_code == code, (
                f'При GET-запросе на {url} от клиента "{name}"'
                f"пришел статус {response.status_code}"
            )
