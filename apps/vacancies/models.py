import uuid

from django.db import models

from apps.attributes.models import City, Occupation, ReviewStatus, WorkFormat
from apps.core.constants import UNCHOSEN_STATUS_ID
from apps.core.models import BaseModel
from apps.employers.models import Employer
from apps.students.models import Applicant


class Vacancy(BaseModel):
    """Модель Вакансии работодателя."""

    id = models.UUIDField(
        "Уникальный id", primary_key=True, default=uuid.uuid4, editable=False
    )
    is_published = models.BooleanField(
        verbose_name="Опубликована", default=True
    )
    creator = models.ForeignKey(Employer, on_delete=models.CASCADE)
    title = models.CharField(verbose_name="Должность", max_length=50)
    attendance = models.ForeignKey(
        WorkFormat, on_delete=models.PROTECT, verbose_name="Тип"
    )
    occupation = models.ForeignKey(
        Occupation, on_delete=models.PROTECT, verbose_name="Занятость"
    )
    description = models.TextField(verbose_name="Описание", max_length=1000)
    min_salary = models.PositiveIntegerField()
    max_salary = models.PositiveIntegerField()
    city = models.ForeignKey(
        City, on_delete=models.PROTECT, verbose_name="Город"
    )
    # stack = models.ManyToManyField(
    #     Stack, through="VacancyStack", verbose_name="Стек инструментов"
    # )

    class Meta:
        verbose_name = "Вакансия"
        verbose_name_plural = "Вакансии"
        default_related_name = "vacancies"

    def __str__(self) -> str:
        return f'Вакансия "{self.title}" для "{self.creator.name}"'


class Respond(BaseModel):
    """Модель отклика на вакансии."""

    applicant = models.ForeignKey(
        Applicant, on_delete=models.CASCADE, verbose_name="Соискатель"
    )
    vacancy = models.ForeignKey(
        Vacancy, on_delete=models.CASCADE, verbose_name="Вакансия"
    )
    status = models.ForeignKey(
        ReviewStatus,
        on_delete=models.PROTECT,
        verbose_name="Статус рассмотрения отклика",
        default=UNCHOSEN_STATUS_ID,
    )

    class Meta:
        verbose_name = "Отклик"
        verbose_name_plural = "Отклики"
        default_related_name = "responds"
        ordering = ("-created_at",)
        constraints = (
            models.UniqueConstraint(
                fields=("vacancy", "applicant"),
                name="Уникальная пара Вакансия - Соискатель",
            ),
        )

    def __str__(self) -> str:
        return f"Отклик {self.applicant} на {self.vacancy}"
