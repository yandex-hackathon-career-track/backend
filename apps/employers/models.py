import uuid

from django.db import models

from apps.attributes.models import ReviewStatus
from apps.core.constants import UNCHOSEN_STATUS_ID
from apps.core.models import BaseModel
from apps.students.models import Applicant
from apps.users.models import CustomUser


class Employer(BaseModel):
    """Профиль работодателя."""

    id = models.UUIDField(
        "Уникальный id", primary_key=True, default=uuid.uuid4, editable=False
    )
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="employer",
        verbose_name="Пользователь",
    )
    name = models.CharField(
        verbose_name="Название компании", max_length=100, blank=True
    )
    about = models.TextField(
        verbose_name="О компании", max_length=1000, blank=True
    )
    website = models.URLField(verbose_name="Ссылка на сайт", blank=True)
    phone = models.CharField(
        verbose_name="Номер телефона", max_length=20, blank=True
    )
    email = models.EmailField(verbose_name="Контактный email", blank=True)
    activity = models.CharField(
        verbose_name="Сфера деятельности", max_length=255, blank=True
    )

    class Meta:
        verbose_name = "Работодатель"
        verbose_name_plural = "Работодатели"

    def __str__(self) -> str:
        return self.name


class SelectedResume(BaseModel):
    """Модель отобранных работодателем соискателей."""

    employer = models.ForeignKey(
        Employer,
        on_delete=models.CASCADE,
        verbose_name="Работодатель",
        related_name="selected_resumes",
    )
    applicant = models.ForeignKey(
        Applicant,
        on_delete=models.CASCADE,
        verbose_name="Соискатель",
        related_name="selected_by",
    )
    status = models.ForeignKey(
        ReviewStatus,
        on_delete=models.PROTECT,
        verbose_name="Статус кандидата",
        default=UNCHOSEN_STATUS_ID,
    )
    comments = models.CharField(
        verbose_name="Комментарии", max_length=255, blank=True
    )

    class Meta:
        verbose_name = "Отобранный соискатель"
        verbose_name_plural = "Отобранные соискатели"
        constraints = (
            models.UniqueConstraint(
                fields=("employer", "applicant"),
                name="Уникальная пара Работодатель - Соискатель",
            ),
        )

    def __str__(self) -> str:
        return f"Кандидат {self.applicant} для {self.employer}"
