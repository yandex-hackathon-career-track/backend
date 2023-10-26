from rest_framework.permissions import BasePermission, SAFE_METHODS

from apps.employers.models import Company
from apps.users.models import Role
from apps.vacancies.models import Vacancy
from apps.vacancies.selectors import user_is_vacancy_creator


class IsEmployerOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        """Создание для работодателей, иначе - только чтение."""
        return request.method in SAFE_METHODS or (
            request.user.is_authenticated
            and request.user.role == Role.EMPLOYER
        )

    def has_object_permission(self, request, view, obj: Company | Vacancy):
        """Работодатель - автор объекта, иначе - только чтение."""
        if isinstance(obj, Company):
            return request.method in SAFE_METHODS or (
                request.user.employer in obj.employers
            )
        return request.method in SAFE_METHODS or (
            request.user.employer == obj.creator
        )


class RespondPermission(BasePermission):
    def has_permission(self, request, view):
        """Создание для соискателей, чтение/изменение - для автора вакансии."""
        if request.method == "POST":
            return (
                request.user.is_authenticated
                and request.user.role == Role.APPLICANT
            )
        user, vacancy_id = request.user, request.kwargs.get("pk")
        return request.user.is_authenticated and user_is_vacancy_creator(
            user, vacancy_id
        )
