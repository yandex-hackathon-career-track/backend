import uuid

from django.db import models

from apps.employers.models import Employer


# УБРАТЬ ПЕРЕД КОММИТОМ
class BaseModel(models.Model):
    """Базовая модель для отслеживания изменений и обновлений."""

    created_at = models.DateTimeField("Дата создания", auto_now_add=True)
    updated_at = models.DateTimeField("Дата обновления", auto_now=True)

    class Meta:
        abstract = True


class VacancyStatus(models.TextChoices):
    OPEN = "open", "открыта"
    CLOSED = "closed", "закрыта"


class Vacancy(BaseModel):
    """Модель Вакансии работодателя."""

    id = models.UUIDField(
        "Уникальный id", primary_key=True, default=uuid.uuid4, editable=False
    )
    author = models.ForeignKey(Employer, on_delete=models.CASCADE)
    status = models.CharField(
        verbose_name="Статус вакансии",
        max_length=10,
        choices=VacancyStatus.choices,
        default=VacancyStatus.OPEN,
    )
    title = models.CharField(verbose_name="Название", max_length=50)
    description = models.TextField(verbose_name="Описание", max_length=1000)
    # tools = models.ManyToManyField("Stack", through="VacancyStack")

    class Meta:
        verbose_name = "Работодатель"
        verbose_name_plural = "Работодатели"
        default_related_name = "vacancies"

    def __str__(self) -> str:
        return f"{self.title} для {self.author.company}"


class VacancyStack(BaseModel):
    """Промежуточная модель для требуемого Стека в Вакансии."""

    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE)
    # stack = models.ForeignKey("Stack", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Инструмент в Вакансии"
        verbose_name_plural = "Инструменты в вакансиях"

    # def __str__(self) -> str:
    #     return f"{self.stack.name} в вакансии {self.vacancy.title}"
