from apps.core.constants import UNCHOSEN_STATUS_ID
from apps.students.models import Applicant

from .models import Respond


def create_respond(applicant: Applicant, vacancy_id: int) -> Respond:
    """Создание нового отклика."""
    return Respond.objects.create(
        applicant=applicant,
        vacancy_id=vacancy_id,
        status_id=UNCHOSEN_STATUS_ID,
    )
