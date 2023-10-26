from django.db import models

from apps.core.models import BaseModel


class Direction(BaseModel):
    """Направление в сфере деятельности."""

    name = models.CharField("Название", max_length=100)

    class Meta:
        verbose_name = "Должность"
        verbose_name_plural = "Должности"

    def __str__(self):
        return self.name


class Contact(BaseModel):
    """Контакты."""

    email = models.EmailField("Email", max_length=255, blank=True, null=True)
    telegram = models.CharField("Telegram", max_length=30, blank=True)

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"

    def __str__(self):
        return f"{self.email}, {self.telegram}"


class City(BaseModel):
    """Город."""

    name = models.CharField("Название", max_length=100)

    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"

    def __str__(self):
        return self.name


class Stack(BaseModel):
    """Стек технологий."""

    name = models.CharField("Название", max_length=100)

    class Meta:
        verbose_name = "Cтек"
        verbose_name_plural = "Cтек"

    def __str__(self):
        return self.name


class WorkFormat(BaseModel):
    """Формат работы."""

    name = models.CharField("Название", max_length=100)

    class Meta:
        verbose_name = "Формат работы"
        verbose_name_plural = "Форматы работы"

    def __str__(self):
        return self.name


class Course(BaseModel):
    """Опыт работы соискателя."""

    name = models.CharField("Название", max_length=100)

    direction = models.ForeignKey(
        Direction, on_delete=models.CASCADE, related_name="course_directions"
    )

    class Meta:
        verbose_name = "Связь курса и направления"
        verbose_name_plural = "Связи курсов и направлений"

    def __str__(self):
        return self.name


class ActivityStatus(BaseModel):
    """Статус активности."""

    name = models.CharField("Название", max_length=100)

    class Meta:
        verbose_name = "Статус активности"
        verbose_name_plural = "Статусы активности"

    def __str__(self):
        return self.name


class ReviewStatus(BaseModel):
    """Статус рассмотрения кандидата/отклика."""

    name = models.CharField("Название", max_length=100)

    class Meta:
        verbose_name = "Статус рассмотрения"
        verbose_name_plural = "Статусы рассмотрения"

    def __str__(self):
        return self.name
