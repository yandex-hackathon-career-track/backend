from rest_framework import serializers

from apps.users.models import CustomUser


class MeUserSerializer(serializers.ModelSerializer):
    """Сериализация данных текущего пользователя."""

    class Meta:
        fields = ("id", "email", "role")
        model = CustomUser
