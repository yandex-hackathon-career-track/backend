from rest_framework.permissions import BasePermission, SAFE_METHODS

from apps.users.models import Role


class IsEmployerOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        """Создание для работодателей, иначе - только чтение."""
        return request.method in SAFE_METHODS or (
            request.user.is_authenticated
            and request.user.role == Role.EMPLOYER
        )

    def has_object_permission(self, request, view, obj):
        """Работодатель связан с компанией, иначе - только чтение."""
        return request.method in SAFE_METHODS or (
            request.user.employer in obj.employers
        )
