from http import HTTPStatus

import pytest


@pytest.mark.django_db()
class Test04Attributes:
    list_url = "/api/v1/attributes/"

    def test_01_access_to_url(self, employer_client, guest_client, vacancy):
        """Аттрибуты доступны всем."""
        expectation = (
            ("гость", guest_client, HTTPStatus.OK),
            ("компания", employer_client, HTTPStatus.OK),
        )
        for name, client, code in expectation:
            response = client.get(self.list_url.format(id=vacancy.id))
            assert response.status_code == code, (
                f'При GET-запросе на {self.list_url} от клиента "{name}"'
                f"пришел статус {response.status_code}"
            )
