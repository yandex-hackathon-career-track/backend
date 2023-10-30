from http import HTTPStatus

import pytest


@pytest.mark.django_db()
class Test05Applicants:
    list_url = "/api/v1/applicants/"

    def test_01_access_to_url(self, employer_client, guest_client):
        """Анкеты соискателей доступны только работодателям."""
        expectation = (
            ("гость", guest_client, HTTPStatus.UNAUTHORIZED),
            ("компания", employer_client, HTTPStatus.OK),
        )
        for name, client, code in expectation:
            response = client.get(self.list_url)
            assert response.status_code == code, (
                f"При GET-запросе списка анкет на {self.list_url} от "
                f"клиента '{name}' пришел статус {response.status_code}"
            )
