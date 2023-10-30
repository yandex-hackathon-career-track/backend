import uuid

from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models


class Role(models.TextChoices):
    """Варианты роли пользователя."""

    APPLICANT = "applicant", "соискатель"
    EMPLOYER = "employer", "работодатель"
    ADMIN = "admin", "администратор"


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """Метод создания обычного пользователя."""
        if not email:
            raise ValueError("Необходимо указать адрес электронной почты")
        email = email.lower()
        user = self.model(email=email, **extra_fields)
        if not password:
            password = self.make_random_password(length=10)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """Метод создания суперпользователя."""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("role", Role.ADMIN)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Суперпользователь должен иметь is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(
                "Суперпользователь должен иметь is_superuser=True."
            )
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """Модель пользователя. Идентификатор - поле email."""

    id = models.UUIDField(
        "Уникальный id", primary_key=True, default=uuid.uuid4, editable=False
    )
    email = models.EmailField(unique=True)

    role = models.CharField(
        verbose_name="Роль",
        max_length=15,
        choices=Role.choices,
        default=Role.EMPLOYER,
    )
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField("Активный", default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
