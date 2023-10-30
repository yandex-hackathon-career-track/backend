from rest_framework import serializers

from apps.core.constants import ACCEPTABLE_FILES, FILE_SIZE_LIMIT
from apps.employers.models import Employer

from ..attributes.serializers import EmployeesNumberSerializer


class BaseEmployerSerializer(serializers.ModelSerializer):
    """Базовый сериализатор данных для профиля Работодателя."""

    class Meta:
        fields = (
            "id",
            "name",
            "about",
            "website",
            "phone",
            "email",
            "activity",
            "foundation_year",
            "employees_number",
            "file",
        )
        model = Employer


class ReadEmployerSerializer(BaseEmployerSerializer):
    """Сериализатор на чтение профиля Работодателя."""

    employees_number = EmployeesNumberSerializer()


class UpdateEmployerSerializer(BaseEmployerSerializer):
    """Сериализатор на изменение профиля Работодателя."""

    def validate_file(self, file):
        type, extension = file.content_type.split("/")
        if extension.lower() not in ACCEPTABLE_FILES:
            raise serializers.ValidationError(
                "Загрузка этого типа файла не поддерживается."
            )
        if file.size > FILE_SIZE_LIMIT:
            raise serializers.ValidationError(
                f"Максимальный размер файла - {FILE_SIZE_LIMIT} Мб"
            )
        return file
