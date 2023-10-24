from django.db import models


class BaseModel(models.Model):
    """Базовая модель для отслеживания изменений и обновлений."""

    created_at = models.DateTimeField("Дата создания", auto_now_add=True)
    updated_at = models.DateTimeField("Дата обновления", auto_now=True)

    class Meta:
        abstract = True
