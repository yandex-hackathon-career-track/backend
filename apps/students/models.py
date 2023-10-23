import uuid

from django.db import models

from apps.attributes.models import City, Contact, Direction, Stack
from apps.core.models import BaseModel
from apps.users.models import CustomUser


class StatusChoices(models.TextChoices):
    ACTIVE = "active", "в активном поиске"
    INACTIVE = "inactive", "не ищу работу"
    HIRED = "hired", "устроен на работу"


class EducationChoices(models.TextChoices):
    MIDDLE = "middle", "среднее"
    HIGH = "high", "высшее"


class WorkFormatChoices(models.TextChoices):
    OFFICE = "office", "офис"
    REMOTE = "remote", "удаленная работа"
    HYBRID = "hybrid", "гибридный формат"


class Applicant(BaseModel):
    """Профиль студента."""

    id = models.UUIDField(
        "Уникальный id",
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="applicant"
    )
    photo = models.ImageField(
        "Фото профиля",
        upload_to="images/students/%Y/%m/%d/",
        default="images/students/default.jpg",
        blank=True,
        null=True
    )
    first_name = models.CharField("Имя", max_length=30)
    last_name = models.CharField("Фамилия", max_length=30)
    experience = models.PositiveIntegerField("Опыт работы, в годах")
    age = models.PositiveIntegerField("Возраст", blank=True, null=True)
    can_relocate = models.BooleanField("Релокация")
    portfolio_link = models.URLField("Ссылка на портфолио", blank=True)
    direction = models.ManyToManyField(
        Direction,
        related_name="applicant",
        verbose_name="Должность"
    )
    stack = models.ManyToManyField(
        Stack,
        related_name="applicant",
        verbose_name="Стек"
    )
    city = models.ManyToManyField(
        City,
        related_name="applicant",
        verbose_name="Город"
    )
    contacts = models.ForeignKey(
        Contact,
        on_delete=models.CASCADE,
        related_name="applicant",
        verbose_name="Контакты",
    )
    status = models.CharField(
        max_length=20,
        choices=StatusChoices.choices,
        verbose_name="Статус активности"
    )
    education_level = models.CharField(
        max_length=20,
        choices=EducationChoices.choices,
        verbose_name="Образование"
    )
    work_format = models.CharField(
        max_length=20,
        choices=WorkFormatChoices.choices,
        verbose_name="Формат работы"
    )

    class Meta:
        verbose_name = "Соискатель"
        verbose_name_plural = "Соискатели"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Course(BaseModel):
    """Курс."""

    name = models.CharField("Название", max_length=30)
    duration = models.PositiveIntegerField("Длительность курса в месяцах")

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

    def __str__(self):
        return f"{self.name}"


class ApplicantCourse(BaseModel):
    """Отслеживание курсов, пройденных соискателями."""

    applicant = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="applicant_course",
        verbose_name="Соискатель"
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="applicant_course",
        verbose_name="Курс"
    )
    graduation_date = models.DateField("Дата окончания курса")
