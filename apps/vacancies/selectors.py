from .models import Vacancy


def get_all_vacancies():
    return Vacancy.objects.prefetch_related("tools")
