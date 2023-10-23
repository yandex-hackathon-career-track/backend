from rest_framework import serializers

from apps.vacancies.models import Vacancy


class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        # добавить tools
        fields = ("id", "author", "status", "title", "description")
        model = Vacancy
        read_only_fields = ("author",)
