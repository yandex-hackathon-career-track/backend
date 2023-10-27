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


def get_vacancy_with_responds(vacancy_id: UUID) -> Vacancy:
    """Поиск вакансии по id с загрузкой откликов и статистикой."""
    queryset = Vacancy.objects.prefetch_related(
        "responds",
        "responds__applicant",
        "responds__applicant__contact",
        "responds__status",
    ).annotate(
        new=Value(0),
        under_review=Value(0),
        sent_test=Value(0),
        interview=Value(0),
        refusal=Value(0),
    )
    return get_object_or_404(queryset, id=vacancy_id)


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
    """Проверка, что соискатель уже откликался на вакансию."""
    return Respond.objects.filter(
        vacancy_id=vacancy_id, applicant=applicant
    ).exists()


def get_respond_by_id(vacancy_id: UUID, respond_id: int) -> Respond:
    """Получение отклика по id вакансии и id отклика"""
    return get_object_or_404(Respond, id=respond_id, vacancy_id=vacancy_id)
