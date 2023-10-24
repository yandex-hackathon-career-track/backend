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


class Contact(models.Model):
    """Контакты."""

    email = models.EmailField("Email", max_length=255, blank=True, null=True)
    phone = models.CharField("Телефон", max_length=20, blank=True)
    telegram = models.CharField(
        "Telegram", max_length=30, blank=True
    )

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"

    def __str__(self):
        return f"{self.email}, {self.phone}, {self.telegram}"


class Course(BaseModel):
    """Курс."""

    name = models.CharField("Название", max_length=30)

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
    

class WorkFormat(models.Model):
    """Формат работы."""
    name = models.CharField("Название", max_length=30, unique=True)

    class Meta:
        verbose_name = "Формат работы"
        verbose_name_plural = "Форматы работы" 

    def __str__(self):
        return self.name