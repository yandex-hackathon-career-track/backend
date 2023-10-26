import uuid

from django.db import models
from datetime import date

from apps.attributes.models import (
    ActivityStatus,
    City,
    Course,
    Contact,
    Stack,
    WorkFormat,
)
from apps.core.models import BaseModel
from apps.users.models import CustomUser


class Applicant(BaseModel):
    """Профиль студента."""

    id = models.UUIDField(
        "Уникальный id", primary_key=True, default=uuid.uuid4, editable=False
    )
    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, related_name="applicant"
    )
    photo = models.ImageField(
        "Фото профиля",
        upload_to="images/students/%Y/%m/%d/",
        default="images/students/default.jpg",
        blank=True,
    )
    first_name = models.CharField("Имя", max_length=30)
    last_name = models.CharField("Фамилия", max_length=30)
    can_relocate = models.BooleanField("Релокация")
    stack = models.ManyToManyField(
        Stack, related_name="applicant", verbose_name="Стек"
    )
    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        related_name="applicant",
        verbose_name="Город",
    )
    contact = models.OneToOneField(
        Contact,
        on_delete=models.SET_NULL,
        null=True,
        related_name="applicant",
        verbose_name="Контакт",
    )
    status = models.ForeignKey(
        ActivityStatus,
        on_delete=models.SET_NULL,
        null=True,
        related_name="applicant",
        verbose_name="Статус",
    )
    work_format = models.ForeignKey(
        WorkFormat,
        on_delete=models.SET_NULL,
        null=True,
        related_name="applicant",
        verbose_name="Формат работы",
    )

    def calculate_total_experience(self):
        total_experience = 0
        for job in self.jobs.all():
            total_experience += job.experience
        return total_experience

    @property
    def total_experience(self):
        return self.calculate_total_experience()

    class Meta:
        verbose_name = "Соискатель"
        verbose_name_plural = "Соискатели"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class ApplicantCourse(BaseModel):
    """Пройденные соискателем курсы."""

    applicant = models.ForeignKey(
        Applicant,
        on_delete=models.CASCADE,
        related_name="applicant_courses",
        verbose_name="Соискатель",
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="applicant_courses",
        verbose_name="Курс",
    )
    graduation_date = models.DateField("Дата окончания курса")

    class Meta:
        verbose_name = "Пройденные курсы"
        verbose_name_plural = "Пройденные курсы"

    def __str__(self):
        return f"{self.applicant} - {self.course} ({self.graduation_date})"


class Job(BaseModel):
    applicant = models.ForeignKey(
        Applicant,
        on_delete=models.CASCADE,
        related_name="jobs",
        verbose_name="Соискатель",
    )
    name = models.CharField("Название", max_length=50)
    start_date = models.DateField("Дата начала работы")
    end_date = models.DateField("Дата окончания работы", null=True, blank=True)
    is_current = models.BooleanField(
        "В настоящее время работает", default=False
    )

    @property
    def experience(self):
        if self.is_current:
            today = date.today()
            delta = today - self.start_date
        elif self.end_date:
            delta = self.end_date - self.start_date
        else:
            return 0

        months = delta.days // 30
        return months

    class Meta:
        verbose_name = "Работа"
        verbose_name_plural = "Работа"

    def __str__(self):
        return self.name


class Education(BaseModel):
    """Образование."""

    applicant = models.ForeignKey(
        Applicant,
        on_delete=models.CASCADE,
        related_name="educations",
        verbose_name="Образование",
    )
    name = models.CharField("Название", max_length=100)

    class Meta:
        verbose_name = "Образование"
        verbose_name_plural = "Образование"

    def __str__(self):
        return self.name


class PortfolioLink(BaseModel):
    """Модель для хранения ссылки на портфолио."""

    applicant = models.ForeignKey(
        Applicant,
        on_delete=models.CASCADE,
        related_name="portfolio_links",
        verbose_name="Ссылка на портфолио",
    )
    name = models.CharField("Имя", max_length=30)
    link = models.URLField("Ссылка на портфолио", blank=True)

    class Meta:
        verbose_name = "Ссылка на портфолио"
        verbose_name_plural = "Ссылка на портфолио"

    def __str__(self):
        return self.name
