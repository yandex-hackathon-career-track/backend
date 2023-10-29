from datetime import datetime

from django.core.exceptions import ValidationError

from apps.core.constants import MIN_FOUNDATION_YEAR


def validate_year(data):
    if data > datetime.now().year:
        raise ValidationError(
            "Год основания не может быть больше текущего года."
        )
    if data <= MIN_FOUNDATION_YEAR:
        raise ValidationError(
            f"Год основания не может быть меньше {MIN_FOUNDATION_YEAR}."
        )
