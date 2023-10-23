from django.db import models

from apps.core.models import BaseModel


class Direction(BaseModel):
    """Направление, должность."""

    name = models.CharField("Название", max_length=100)

    class Meta:
        verbose_name = "Должность"
        verbose_name_plural = "Должности"

    def __str__(self):
        return self.name


class Course(BaseModel):
    """Курс."""

    name = models.CharField("Название", max_length=30)
    duration = models.PositiveIntegerField("Длительность курса в месяцах")

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

    def __str__(self):
        return f"{self.name}"


class City(BaseModel):
    """Город."""

    name = models.CharField("Город", max_length=20, unique=True)
    slug = models.SlugField("Слаг", unique=True)

    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"

    def __str__(self):
        return self.name


class Stack(BaseModel):
    """Стек технологий."""

    name = models.CharField("Стек", max_length=20, unique=True)
    slug = models.SlugField("Слаг", unique=True)

    class Meta:
        verbose_name = "Cтек"
        verbose_name_plural = "Cтек"

    def __str__(self):
        return self.name
