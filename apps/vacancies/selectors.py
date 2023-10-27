from uuid import UUID

from django.db.models import QuerySet, Value
from django.shortcuts import get_object_or_404

from apps.users.models import CustomUser

from .models import Vacancy


def add_all_associated_tables(queryset: QuerySet) -> QuerySet:
    """Загрузка сопутствующих таблиц."""
    return queryset.select_related("city", "creator")


def add_annotation(queryset: QuerySet) -> QuerySet:
    """Аннотация статистикой по вакансии."""
    return queryset.annotate(
        views_qty=Value(0),
        responds_qty=Value(0),
        total_resume_qty=Value(0),
        chosen_resume_qty=Value(0),
    )


def get_employer_vacancies_by_user(user: CustomUser, action: str) -> QuerySet:
    """Выгрузка всех вакансий пользователя-работодателя."""
    vacancies = user.employer.vacancies
    if action == "list":
        return add_annotation(vacancies)
    if action == "retrieve":
        return add_all_associated_tables
    return vacancies


def get_vacancy_responds(vacancy_id: UUID) -> QuerySet:
    """Выгрузка всех откликов на вакансию."""
    vacancy = get_object_or_404(Vacancy, id=vacancy_id)
    return vacancy.responds.select_related(
        "applicant", "applicant__contact", "status"
    )


def user_is_vacancy_creator(user: CustomUser, vacancy_id: UUID) -> bool:
    return Vacancy.objects.filter(creator__user=user, id=vacancy_id).exists()
