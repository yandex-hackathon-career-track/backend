from uuid import UUID

from django.core.exceptions import ObjectDoesNotExist

from apps.core.exceptions import ObjectAlreadyExistsException

from .models import CustomUser, SelectedResume


def add_to_selected(user: CustomUser, applicant_id: UUID) -> None:
    """Добавление соискателя в Избранное."""
    if user.employer.selected_resumes.filter(
        applicant_id=applicant_id
    ).exists():
        raise ObjectAlreadyExistsException(
            "Соискатель уже добавлен в избранное"
        )
    SelectedResume.objects.create(
        applicant_id=applicant_id, employer=user.employer
    )
    return None


def remove_from_selected(user: CustomUser, applicant_id: UUID) -> None:
    """Удаление соискателя из Избранного."""
    deleted, _ = user.employer.selected_resumes.filter(
        applicant_id=applicant_id
    ).delete()
    if not deleted:
        raise ObjectDoesNotExist("Соискатель не был в Избранном.")
    return None
