from djoser.serializers import UserCreateSerializer
from rest_framework import serializers

from apps.users.models import CustomUser, Role
from apps.users.services import create_user_with_profile


class MeUserSerializer(serializers.ModelSerializer):
    """Сериализация данных текущего пользователя."""

    profile_id = serializers.SerializerMethodField()

    class Meta:
        fields = ("id", "email", "role", "profile_id")
        model = CustomUser

    def get_profile_id(self, obj: Role):
        if obj.role == Role.EMPLOYER:
            return obj.employer.id
        if obj.role == Role.APPLICANT:
            return obj.applicant.id
        return None


class MyUserCreateSerializer(UserCreateSerializer):
    """Сериализатор создания пользователя на базе Djoser."""

    def perform_create(self, validated_data):
        return create_user_with_profile(validated_data)
