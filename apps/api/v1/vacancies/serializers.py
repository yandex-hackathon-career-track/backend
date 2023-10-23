from rest_framework import serializers

from apps.vacancies.models import Vacancy

from ..employers.serializers import CompanySerializer


class VacancySerializer(serializers.ModelSerializer):
    company = CompanySerializer(source="creator.company", read_only=True)

    class Meta:
        # добавить tools
        fields = ("id", "creator", "company", "status", "title", "description")
        model = Vacancy
        read_only_fields = ("creator", "company")
