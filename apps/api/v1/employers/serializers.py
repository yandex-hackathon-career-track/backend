from rest_framework import serializers

from apps.employers.models import Employer


class EmployerSerializer(serializers.ModelSerializer):
    """Сериализация данных для профиля Работодателя."""

    class Meta:
        fields = (
            "id",
            "name",
            "about",
            "website",
            "phone",
            "email",
            "activity",
        )
        model = Employer
