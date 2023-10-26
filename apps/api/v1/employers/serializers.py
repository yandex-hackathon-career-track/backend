from rest_framework import serializers

from apps.employers.models import Company, Employer


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
