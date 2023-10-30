import pytest

from apps.vacancies.models import Vacancy


@pytest.fixture
def vacancy(employer_user, city, full_occupation, remote_format):
    return Vacancy.objects.create(
        creator=employer_user.employer,
        city_id=city.id,
        occupation_id=full_occupation.id,
        attendance_id=remote_format.id,
        title="Разработчик на PHP",
        is_published=True,
        description="Много слов и много требований прямо тут",
        min_salary=100000,
        max_salary=300000,
    )
