from django.db import models

from apps.core.models import BaseModel, NamedModel


class Contact(BaseModel):
    """Контакты."""

    email = models.EmailField("Email", max_length=255, blank=True, null=True)
    telegram = models.CharField("Telegram", max_length=30, blank=True)

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"

    def __str__(self):
        return f"{self.email}, {self.telegram}"


class Direction(NamedModel):
    """Направление в сфере деятельности."""

    class Meta:
        verbose_name = "Направление"
        verbose_name_plural = "Направления"


class City(NamedModel):
    """Город."""

    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"


class Stack(NamedModel):
    """Стек технологий."""

    class Meta:
        verbose_name = "Cтек"
        verbose_name_plural = "Cтек"


class WorkFormat(NamedModel):
    """Формат работы."""

    class Meta:
        verbose_name = "Формат работы"
        verbose_name_plural = "Форматы работы"


class Course(NamedModel):
    """Курсы Практикума."""

    direction = models.ForeignKey(
        Direction, on_delete=models.CASCADE, related_name="course_directions"
    )

    class Meta:
        verbose_name = "Курс Практикума"
        verbose_name_plural = "Курсы Практикума"


class ActivityStatus(NamedModel):
    """Статус активности."""

    class Meta:
        verbose_name = "Статус активности"
        verbose_name_plural = "Статусы активности"


class ReviewStatus(NamedModel):
    """Статус рассмотрения кандидата/отклика."""

    class Meta:
        verbose_name = "Статус рассмотрения"
        verbose_name_plural = "Статусы рассмотрения"


class Occupation(NamedModel):
    """Модель занятости."""

    class Meta:
        verbose_name = "Тип занятости"
        verbose_name_plural = "Типы занятости"


class EmployeesNumber(NamedModel):
    """Модель с вариантами численности сотрудников."""

    class Meta:
        verbose_name = "Численность сотрудников"
        verbose_name_plural = "Численность сотрудников"
