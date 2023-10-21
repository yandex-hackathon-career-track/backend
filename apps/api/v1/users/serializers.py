from rest_framework import serializers

from apps.users.models import CustomUser


class MeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id", "email", "role")
        model = CustomUser
