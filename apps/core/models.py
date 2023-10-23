from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    """Базовая модель для отслеживания изменений и обновлений."""

    created_at = models.DateTimeField("Дата создания", auto_now_add=True)
    updated_at = models.DateTimeField("Дата обновления", auto_now=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super(BaseModel, self).save(*args, **kwargs)
