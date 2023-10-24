import uuid

from django.db import models

from apps.attributes.models import Contact
from apps.core.models import BaseModel
from apps.students.models import Applicant
from apps.users.models import CustomUser


class Company(BaseModel):
    """Модель компании-работодателя."""

    name = models.CharField(verbose_name="Название компании", max_length=100)
    about = models.TextField(verbose_name="О компании", max_length=1000)
    website = models.URLField(verbose_name="Ссылка на сайт")

    class Meta:
        verbose_name = "Компания"
        verbose_name_plural = "Компании"


class Employer(BaseModel):
    """Профиль сотрудника работодателя."""

    id = models.UUIDField(
        "Уникальный id", primary_key=True, default=uuid.uuid4, editable=False
    )
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="employer",
        verbose_name="Пользователь",
    )
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name="employers",
        verbose_name="Компания",
    )
    contacts = models.OneToOneField(
        Contact, on_delete=models.SET_NULL, null=True, verbose_name="Контакты"
    )

    class Meta:
        verbose_name = "Работодатель"
        verbose_name_plural = "Работодатели"


class Candidate(BaseModel):
    """Модель отобранных работодателем кандидатов."""

    class Status(models.TextChoices):
        NEW = "new", "новый"

    employer = models.ForeignKey(
        Employer, on_delete=models.CASCADE, verbose_name="Работодатель"
    )
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    status = models.CharField(
        verbose_name="Статус кандидата",
        choices=Status.choices,
        default=Status.NEW,
    )
    comments = models.CharField(verbose_name="Комментарии", max_length=255)

    class Meta:
        verbose_name = "Кандидат"
        verbose_name_plural = "Кандидаты"
        default_related_name = "candidates"
        constraints = (
            models.UniqueConstraint(
                fields=("employer", "applicant"),
                name="Уникальная пара Работодатель - Соискатель",
            ),
        )

    def __str__(self) -> str:
        return f"Кандидат self.applicant для {self.employer}"
