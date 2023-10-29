from uuid import UUID

from django.db.models import Count, Q, QuerySet, Value
from django.shortcuts import get_object_or_404

from apps.core import constants
from apps.employers.models import Employer
from apps.students.models import Applicant
from apps.users.models import CustomUser

from .models import Respond, Vacancy


def add_vacancy_associated_tables(queryset: QuerySet) -> QuerySet:
    """Загрузка таблиц атрибутов для Вакансии."""
    return queryset.select_related("city", "attendance", "occupation")


def add_responds_associated_tables(queryset: QuerySet) -> QuerySet:
    """Загрузка таблиц откликов для Вакансии."""
    return queryset.prefetch_related(
        "responds",
        "responds__applicant",
        "responds__applicant__contact",
        "responds__status",
    )


def add_vacancy_statistics(queryset: QuerySet) -> QuerySet:
    """Аннотация статистикой по вакансии."""
    return queryset.annotate(
        views_qty=Value(278),
        responds_qty=Count("responds"),
        chosen_resume_qty=Count(
            "responds",
            filter=Q(responds__status_id__in=constants.CHOSEN_STATUS_IDS),
        ),
    )


def count_responds_status(status_id):
    """Вспомогательная функция-счетчик статусов для аннотации."""
    return Count("responds", filter=Q(responds__status_id=status_id))


def add_responds_statistics(queryset: QuerySet) -> QuerySet:
    """Аннотация статистикой по откликам на вакансию."""
    return queryset.annotate(
        new=count_responds_status(constants.UNCHOSEN_STATUS_ID),
        under_review=count_responds_status(constants.UNDER_REVIEW_STATUS_ID),
        sent_test=count_responds_status(constants.SENT_TEST_STATUS_ID),
        interview=count_responds_status(constants.INTERVIEW_STATUS_ID),
        refusal=count_responds_status(constants.REFUSAL_STATUS_ID),
    )


def get_employer_vacancies_by_user(user: CustomUser, action: str) -> QuerySet:
    """Выгрузка всех вакансий пользователя-работодателя."""
    vacancies = user.employer.vacancies
    if action == "list" and vacancies:
        return add_vacancy_statistics(vacancies)
    if action == "retrieve":
        return add_vacancy_associated_tables(queryset=vacancies)
    return vacancies


def get_published_vacancies() -> QuerySet:
    """Выгрузка всех вакансий на сайте."""
    return Vacancy.objects.filter(is_published=True).select_related(
        "city", "attendance", "occupation", "creator"
    )


def get_vacancy_with_responds(
    vacancy_id: UUID, prefetch_required: bool = True
) -> Vacancy:
    """Поиск вакансии по id с загрузкой откликов и статистикой."""
    queryset = Vacancy.objects.all()
    queryset = add_responds_statistics(queryset)
    if prefetch_required:
        queryset = add_responds_associated_tables(queryset)
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
    """Получение отклика по id вакансии и id отклика."""
    return get_object_or_404(Respond, id=respond_id, vacancy_id=vacancy_id)


def count_resumes_for_vacancy(vacancy: Vacancy) -> int:
    """Подсчет резюме подходящих под критерии вакансии."""
    return Applicant.objects.filter(
        city=vacancy.city,
        work_format=vacancy.attendance,
        occupation=vacancy.occupation,
    ).count()
