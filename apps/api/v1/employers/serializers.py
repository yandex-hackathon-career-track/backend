from rest_framework import serializers

from apps.employers.models import Employer, SelectedResume
from apps.employers.selectors import relation_exists


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


class SelectedResumeSerializer(serializers.ModelSerializer):
    """Сериализация отбора резюме."""

    status = serializers.BooleanField(required=False)

    class Meta:
        model = SelectedResume
        fields = ("id", "status")

    def validate(self, data):
        applicant_id = self.context.get("view").kwargs.get("id")
        user = self.context.get("request").user
        if relation_exists(user, applicant_id, self.instance):
            raise serializers.ValidationError(
                "Соискатель уже добавлен в Избранное."
            )
        return super().validate(data)
