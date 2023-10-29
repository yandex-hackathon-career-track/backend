from django.db import models


class BaseModel(models.Model):
    """Базовая модель для отслеживания изменений и обновлений."""

    created_at = models.DateTimeField("Дата создания", auto_now_add=True)
    updated_at = models.DateTimeField("Дата обновления", auto_now=True)

    class Meta:
        abstract = True


class NamedModel(models.Model):
    """Модель с именем для атрибутов."""

    name = models.CharField("Название", max_length=100, unique=True)

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return self.name
