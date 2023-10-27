from uuid import UUID

from django.db.models import QuerySet, Value
from django.shortcuts import get_object_or_404

from apps.employers.models import Employer
from apps.users.models import CustomUser

from .models import Respond, Vacancy


def add_all_associated_tables(queryset: QuerySet) -> QuerySet:
    """Загрузка сопутствующих таблиц."""
    return queryset.select_related("city", "attendance", "occupation")


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
        return add_all_associated_tables(queryset=vacancies)
    return vacancies


def get_published_vacancies() -> QuerySet:
    """Выгрузка всех вакансий на сайте."""
    return Vacancy.objects.filter(is_published=True).select_related(
        "city", "attendance", "occupation", "creator"
    )


def get_vacancy_responds(vacancy_id: UUID) -> QuerySet:
    """Выгрузка всех откликов на вакансию."""
    vacancy = get_object_or_404(Vacancy, id=vacancy_id)
    return vacancy.responds.select_related(
        "applicant", "applicant__contact", "status"
    )


def user_is_vacancy_creator(user: CustomUser, vacancy_id: UUID) -> bool:
    """Проверка, что пользователь - создатель вакансии"""
    return Vacancy.objects.filter(creator__user=user, id=vacancy_id).exists()


def same_titled_vacancy_exists(
    title: str, employer: Employer, instance: Vacancy | None
) -> bool:
    """Проверка, что у работодателя есть активная вакансия на эту должность."""
    vacancy = Vacancy.objects.filter(
        title=title, creator=employer, is_published=True
    )
    if instance:
        vacancy.exclude(pk=instance.pk)
    return vacancy.exists()


def already_responded(vacancy_id: int, applicant) -> bool:
    return Respond.objects.filter(
        vacancy_id=vacancy_id, applicant=applicant
    ).exists()
