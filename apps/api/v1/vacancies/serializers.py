from rest_framework import serializers

from apps.students.models import Applicant
from apps.vacancies.models import Vacancy, Respond

from ..attributes.serializers import (
    ReviewStatusSerializer,
    WorkFormatSerializer,
    OccupationSerializer,
    CitySerializer,
)


class BaseVacancySerializer(serializers.ModelSerializer):
    """Базовый сериализатор для вакансий работодателя."""

    is_published = serializers.BooleanField(required=False)

    class Meta:
        fields = ("id", "title", "is_published", "created_at", "updated_at")
        model = Vacancy
        read_only_fields = ("created_at", "updated_at")


class UnsafeVacancySerializer(BaseVacancySerializer):
    """Сериализация создания/изменения полей вакансий в ЛК работодателя."""

    is_published = serializers.BooleanField(required=False)

    class Meta(BaseVacancySerializer.Meta):
        fields = BaseVacancySerializer.Meta.fields + (
            "attendance",
            "occupation",
            "description",
            "min_salary",
            "max_salary",
            "city",
        )


class ListVacancySerializer(BaseVacancySerializer):
    """Сериализация для списка вакансий в ЛК работодателя."""

    views_qty = serializers.IntegerField()
    responds_qty = serializers.IntegerField()
    total_resume_qty = serializers.IntegerField()
    chosen_resume_qty = serializers.IntegerField()

    class Meta(BaseVacancySerializer.Meta):
        fields = BaseVacancySerializer.Meta.fields + (
            "views_qty",
            "responds_qty",
            "total_resume_qty",
            "chosen_resume_qty",
        )


class DetailVacancySerializer(BaseVacancySerializer):
    """Сериализация для 1 вакансии работодателя."""

    attendance = WorkFormatSerializer()
    occupation = OccupationSerializer()
    city = CitySerializer()

    class Meta(BaseVacancySerializer.Meta):
        fields = BaseVacancySerializer.Meta.fields + (
            "attendance",
            "occupation",
            "description",
            "min_salary",
            "max_salary",
            "city",
        )
        model = Vacancy


class ApplicantInRespondSerializer(serializers.ModelSerializer):
    """Сериализация полей соискателя."""

    email = serializers.EmailField(source="contact.email")
    telegram = serializers.CharField(source="contact.telegram")

    class Meta:
        fields = ("id", "first_name", "last_name", "email", "telegram")
        model = Applicant


class BaseRespondSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id", "applicant", "status")
        model = Respond


class UnsafeRespondSerializer(BaseRespondSerializer):
    pass


class GetRespondSerializer(BaseRespondSerializer):
    applicant = ApplicantInRespondSerializer
    status = ReviewStatusSerializer
