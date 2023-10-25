from djoser.serializers import UserCreateSerializer
from rest_framework import serializers

from apps.users.models import CustomUser
from apps.users.services import create_user_with_profile


class MeUserSerializer(serializers.ModelSerializer):
    """Сериализация данных текущего пользователя."""

    class Meta:
        fields = ("id", "email", "role")
        model = CustomUser


class MyUserCreateSerializer(UserCreateSerializer):
    """Сериализатор создания пользователя на базе Djoser."""

    def perform_create(self, validated_data):
        return create_user_with_profile(validated_data)
