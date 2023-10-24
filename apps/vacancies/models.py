import uuid

from django.db import models

from apps.attributes.models import Stack
from apps.core.models import BaseModel
from apps.employers.models import Employer


class Vacancy(BaseModel):
    """Модель Вакансии работодателя."""

    id = models.UUIDField(
        "Уникальный id", primary_key=True, default=uuid.uuid4, editable=False
    )
    is_published = models.BooleanField(verbose_name="Опубликована")
    creator = models.ForeignKey(Employer, on_delete=models.CASCADE)
    title = models.CharField(verbose_name="Название", max_length=50)
    description = models.TextField(verbose_name="Описание", max_length=1000)
    stack = models.ManyToManyField(
        Stack, through="VacancyStack", verbose_name="Стек инструментов"
    )

    class Meta:
        verbose_name = "Работодатель"
        verbose_name_plural = "Работодатели"
        default_related_name = "vacancies"

    def __str__(self) -> str:
        return f"{self.title} для {self.creator.company}"


class VacancyStack(BaseModel):
    """Промежуточная модель для требуемого Стека в Вакансии."""

    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE)
    stack = models.ForeignKey(Stack, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Инструмент в Вакансии"
        verbose_name_plural = "Инструменты в вакансиях"

    def __str__(self) -> str:
        return f"{self.stack.name} в вакансии {self.vacancy.title}"
