from http import HTTPStatus

import pytest

from .utils import vacancy_utils as utils
from .utils.employer_utils import GOOD_PROFILE


@pytest.mark.django_db()
class Test03Vacancy:
    list_url = "/api/v1/employers/vacancies/"
    detail_url = "/api/v1/employers/vacancies/{id}/"

    def test_01_access_to_url(self, employer_client, guest_client, vacancy):
        """Разделы 'Мои вакансии'/'1 вакансия' доступны только компании."""
        urls = [self.list_url, self.detail_url.format(id=vacancy.id)]
        expectation = (
            ("гость", guest_client, HTTPStatus.UNAUTHORIZED),
            ("компания", employer_client, HTTPStatus.OK),
        )
        for url in urls:
            for name, client, code in expectation:
                response = client.get(url)
                assert response.status_code == code, (
                    f'При GET-запросе на {url} от клиента "{name}"'
                    f"пришел статус {response.status_code}"
                )

    def test_02_create_vacancy_success(
        self, employer_client, remote_format, city, full_occupation
    ):
        """Успешное создание новой вакансии только с заполненным профилем."""
        data = utils.GOOD_VACANCY_DATA
        data["attendance"] = remote_format.id
        data["occupation"] = full_occupation.id
        data["city"] = city.id

        response = employer_client.post(self.list_url, data=data)
        assert (
            response.status_code == HTTPStatus.BAD_REQUEST
        ), "Работодатель с пустым профилем смог создать вакансию."

        employer_client.patch("/api/v1/employers/me/", data=GOOD_PROFILE)

        response = employer_client.post(self.list_url, data=data)
        assert (
            response.status_code == HTTPStatus.CREATED
        ), "Работодатель с заполненным профилем не смог создать вакансию."

    def test_03_publish_filter(self, employer_client, vacancy):
        """Работа фильтров вакансий опубликована/нет, снятие с публикации."""
        published_url = self.list_url + "?is_published=true"
        unpublished_url = self.list_url + "?is_published=false"
        edit_url = self.detail_url.format(id=vacancy.id)

        response = employer_client.get(published_url)
        published_qty = len(response.data)

        response = employer_client.get(unpublished_url)
        unpublished_qty = len(response.data)

        employer_client.patch("/api/v1/employers/me/", data=GOOD_PROFILE)
        r = employer_client.patch(edit_url, data={"is_published": False})
        assert (
            r.status_code == HTTPStatus.OK
        ), "Не удалось снять вакансию с публикации."

        response = employer_client.get(published_url)
        new_published_qty = len(response.data)

        response = employer_client.get(unpublished_url)
        new_unpublished_qty = len(response.data)

        assert (
            published_qty - new_published_qty == 1
        ), "Фильтр активных вакансий работает некорректно."
        assert (
            new_unpublished_qty - unpublished_qty == 1
        ), "Фильтр вакансий в архиве работает некорректно."
