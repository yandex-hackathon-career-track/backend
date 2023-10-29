from django.db import transaction

from apps.employers.models import Employer

from .models import CustomUser, Role


@transaction.atomic
def create_user_with_profile(validated_data: dict) -> CustomUser:
    """Создание пользователя с профилем в соответствии с выбранной ролью."""
    user = CustomUser.objects.create_user(**validated_data)
    role = validated_data.get("role", Role.EMPLOYER)
    if role == Role.EMPLOYER:
        Employer.objects.create(user=user, email=user.email)
    return user
