from django_filters import rest_framework as filters

from apps.vacancies.models import Vacancy


class VacancyFilter(filters.FilterSet):
    class Meta:
        model = Vacancy
        fields = ("is_published",)
