import uuid

from django.db import models
from datetime import datetime

from apps.attributes.models import City, Course, Direction, Stack
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
        blank=True
    )
    first_name = models.CharField("Имя", max_length=30)
    last_name = models.CharField("Фамилия", max_length=30)
    exp_start = models.DateField("Дата начала опыта работы", blank=True, null=True)
    birthday = models.DateField("Дата рождения", blank=True, null=True)
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
    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        related_name="applicant",
        verbose_name="Город"
    )
    phone = models.CharField("Телефон", max_length=20, blank=True, null=True)
    email = models.EmailField("Email", max_length=255, blank=True, null=True)
    telegram = models.URLField("Telegram", blank=True, null=True)
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

    @property
    def experience(self):
        if self.exp_start:
            today = datetime.now().date()
            return today.year - self.exp_start.year

    @property
    def age(self):
        if self.birthday:
            today = datetime.now().date()
            age = (
                today.year - self.birthday.year
                - ((today.month, today.day)
                < (self.birthday.month, self.birthday.day))
            )
            return age

    class Meta:
        verbose_name = "Соискатель"
        verbose_name_plural = "Соискатели"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


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

    class Meta:
        verbose_name = "Пройденные курсы"
        verbose_name_plural = "Пройденные курсы"

    def __str__(self):
        return f"{self.applicant} - {self.course} ({self.graduation_date})"
