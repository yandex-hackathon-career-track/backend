import uuid

from django.db import models
from datetime import date

from apps.attributes.models import (
    City,
    Course,
    Contact,
    Direction,
    Education,
    Status,
    Job,
    PortfolioLink,
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
    portfolio_links = models.ManyToManyField(
        PortfolioLink,
        related_name="applicant",
        verbose_name="Портфолио",
    )
    jobs = models.ManyToManyField(
        Job,
        through="ApplicantJob",
        related_name="jobs",
        verbose_name="Должности",
    )
    courses = models.ManyToManyField(
        Course,
        through="ApplicantCourse",
        related_name="applicants",
        verbose_name="Пройденные курсы",
    )
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
    work_format = models.ForeignKey(
        WorkFormat,
        on_delete=models.SET_NULL,
        null=True,
        related_name="applicant",
        verbose_name="Формат работы",
    )
    education = models.ForeignKey(
        Education,
        on_delete=models.SET_NULL,
        null=True,
        related_name="applicants",
        verbose_name="Образование",
    )
    status = models.ForeignKey(
        Status,
        on_delete=models.SET_NULL,
        null=True,
        related_name="status",
        verbose_name="Статус",
    )

    def calculate_total_experience(self):
        total_experience = 0
        for applicant_job in self.applicant_jobs.all():
            total_experience += applicant_job.experience
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


class ApplicantJob(models.Model):
    """Опыт работы соискателя."""

    applicant = models.ForeignKey(
        Applicant,
        on_delete=models.CASCADE,
        related_name="applicant_jobs",
        verbose_name="Соискатель",
    )
    job = models.ForeignKey(
        Job,
        on_delete=models.CASCADE,
        related_name="applicant_jobs",
        verbose_name="Должность",
    )
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
        verbose_name = "Опыт работы"
        verbose_name_plural = "Опыт работы"


class CourseDirection(models.Model):
    """Опыт работы соискателя."""

    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="course_directions"
    )
    direction = models.ForeignKey(
        Direction, on_delete=models.CASCADE, related_name="course_directions"
    )

    class Meta:
        verbose_name = "Связь курса и направления"
        verbose_name_plural = "Связи курсов и направлений"

    def __str__(self):
        return f"{self.course} - {self.direction}"
