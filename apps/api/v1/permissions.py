from rest_framework.permissions import BasePermission, SAFE_METHODS

from apps.employers.models import Company
from apps.users.models import Role
from apps.vacancies.models import Vacancy


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
            request.user.employer == obj.author
        )
