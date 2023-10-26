from rest_framework import viewsets

from apps.vacancies.selectors import (
    get_employer_vacancies_by_user,
    get_vacancy_responds,
)

from ..permissions import IsEmployerOrReadOnly, VacancyPermission
from . import serializers as ser


class VacancyViewset(viewsets.ModelViewSet):
    """Просмотр, создание, изменение, удаление вакансий."""

    permission_classes = (IsEmployerOrReadOnly,)
    http_method_names = ["get", "post", "patch"]

    def get_serializer_class(self):
        serializer_storage = {
            "list": ser.ListVacancySerializer,
            "retrieve": ser.DetailVacancySerializer,
            "create": ser.UnsafeVacancySerializer,
            "partial_update": ser.UnsafeVacancySerializer,
        }
        return serializer_storage.get(self.action)

    def get_queryset(self):
        return get_employer_vacancies_by_user(
            user=self.request.user, action=self.action
        )

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user.employer)


class RespondViewSet(viewsets.ModelViewSet):
    """Просмотр и изменение статуса откликов на вакансии."""

    permission_classes = (VacancyPermission,)
    http_method_names = ["get", "post", "patch", "delete"]

    def get_queryset(self):
        vacancy_id = self.kwargs.get("pk")
        return get_vacancy_responds(vacancy_id=vacancy_id)

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return ser.GetRespondSerializer
        return ser.UnsafeRespondSerializer
