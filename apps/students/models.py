import uuid

from django.db import models
from datetime import datetime, date

from attributes.models import City, Course, Contact, Direction, Stack, WorkFormat
from core.models import BaseModel
from users.models import CustomUser


class StatusChoices(models.TextChoices):
    ACTIVE = "active", "в активном поиске"
    INACTIVE = "inactive", "не ищу работу"
    HIRED = "hired", "устроен на работу"


class EducationChoices(models.TextChoices):
    MIDDLE = "middle", "среднее"
    HIGH = "high", "высшее"


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
    birthday = models.DateField("Дата рождения", blank=True)
    can_relocate = models.BooleanField("Релокация")
    portfolio_link = models.URLField("Ссылка на портфолио", blank=True)
    directions = models.ManyToManyField(
        Direction,
        through='ApplicantDirection',
        related_name='applicants',
        verbose_name='Должности'
    )
    courses = models.ManyToManyField(
        Course,
        through='ApplicantCourse',
        related_name='applicants',
        verbose_name='Пройденные курсы'
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
    contact = models.OneToOneField(
        Contact,
        on_delete=models.SET_NULL,
        null=True,
        related_name="applicant",
        verbose_name="Контакт"
    )
    work_format = models.ForeignKey(
        WorkFormat,
        on_delete=models.SET_NULL,
        null=True,
        related_name="applicant",
        verbose_name="Формат работы"
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
    """Пройденные соискателем курсы."""

    applicant = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="applicant_courses",
        verbose_name="Соискатель"
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="applicant_courses",
        verbose_name="Курс"
    )
    graduation_date = models.DateField("Дата окончания курса")

    class Meta:
        verbose_name = "Пройденные курсы"
        verbose_name_plural = "Пройденные курсы"

    def __str__(self):
        return f"{self.applicant} - {self.course} ({self.graduation_date})"


class ApplicantDirection(models.Model):
    """Опыт работы соискателя."""
    applicant = models.ForeignKey(
        Applicant, 
        on_delete=models.CASCADE, 
        related_name="applicant_directions",
        verbose_name="Соискатель"
    )
    direction = models.ForeignKey(
        Direction, 
        on_delete=models.CASCADE,
        related_name="applicant_directions",
        verbose_name="Должность"
        )
    start_date = models.DateField("Дата начала работы")
    end_date = models.DateField("Дата окончания работы", null=True, blank=True)
    is_current = models.BooleanField("В настоящее время работает", default=False)

    def calculate_experience(self):
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
        verbose_name = "Опыт работы"
        verbose_name_plural = "Опыт работы"
