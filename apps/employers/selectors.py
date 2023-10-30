from uuid import UUID

from django.shortcuts import get_object_or_404

from .models import CustomUser, Employer, SelectedResume


def get_selected_relation(
    employer: Employer, applicant_id: UUID
) -> SelectedResume:
    """Получение связи Отобранное резюме по работодателю и соискателю."""
    return get_object_or_404(
        SelectedResume, employer=employer, applicant_id=applicant_id
    )


def relation_exists(
    user: CustomUser, applicant_id: UUID, instance: SelectedResume | None
) -> bool:
    """Проверка, что соискатель добавлен в избранные резюме."""
    relation = user.employer.selected_resumes.filter(applicant_id=applicant_id)
    if instance:
        relation.exclude(pk=instance.pk)
    return relation.exists()
