import uuid

from django.db import models

from apps.users.models import CustomUser


# УБРАТЬ ПЕРЕД КОММИТОМ
class BaseModel(models.Model):
    """Базовая модель для отслеживания изменений и обновлений."""

    created_at = models.DateTimeField("Дата создания", auto_now_add=True)
    updated_at = models.DateTimeField("Дата обновления", auto_now=True)

    class Meta:
        abstract = True


class Company(BaseModel):
    """Модель компании-работодателя."""

    title = models.CharField(verbose_name="Название компании", max_length=100)
    about = models.TextField(verbose_name="О компании", max_length=1000)
    website = models.URLField(verbose_name="Ссылка на сайт")

    class Meta:
        verbose_name = "Компания"
        verbose_name_plural = "Компании"


class Employer(BaseModel):
    """Профиль работодателя."""

    id = models.UUIDField(
        "Уникальный id", primary_key=True, default=uuid.uuid4, editable=False
    )
    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, related_name="employer"
    )
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name="employers"
    )
    # contacts = models.OneToOneField(
    #     "Contact", on_delete=models.SET_NULL, null=True
    # )

    class Meta:
        verbose_name = "Работодатель"
        verbose_name_plural = "Работодатели"
