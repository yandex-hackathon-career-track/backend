from rest_framework import serializers

from apps.employers.models import CandidateStatus, Company, Employer


class CompanySerializer(serializers.ModelSerializer):
    """Сериализация данных для Компании."""

    class Meta:
        fields = ("id", "name", "about", "website")
        model = Company


class EmployerSerializer(serializers.ModelSerializer):
    """Сериализация данных для профиля Работодателя."""

    class Meta:
        fields = ("id", "company")
        model = Employer


class CandidateStatusSerializer(serializers.ModelSerializer):
    """Сериализация данных для статусов кандидатов."""

    class Meta:
        fields = ("id", "name")
        model = CandidateStatus
