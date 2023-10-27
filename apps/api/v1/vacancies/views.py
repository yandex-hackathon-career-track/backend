from django.shortcuts import get_object_or_404
from rest_framework import viewsets, mixins, decorators, response, status

from apps.vacancies.models import Vacancy
from apps.vacancies.selectors import (
    get_published_vacancies,
    get_employer_vacancies_by_user,
    get_vacancy_responds,
)

from ..permissions import IsApplicant, IsEmployer, RespondPermission
from . import serializers as ser


class MyVacancyViewset(viewsets.ModelViewSet):
    """Просмотр, создание, изменение, удаление вакансий."""

    permission_classes = (IsEmployer,)
    http_method_names = ["get", "post", "patch"]

    def get_serializer_class(self):
        serializer_storage = {
            "list": ser.ListVacancySerializer,
            "retrieve": ser.DetailMyVacancySerializer,
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


class VacancyViewset(viewsets.ReadOnlyModelViewSet):
    """Просмотр вакансий и создание отклика отклика."""

    permission_classes = (IsApplicant,)
    queryset = get_published_vacancies()
    serializer_class = ser.DetailVacancySerializer

    @decorators.action(methods=["post"], detail=True)
    def respond(self, request, pk):
        vacancy = get_object_or_404(Vacancy, id=pk)
        serializer = ser.CreateRespondSerializer(
            data=request.data, context={"view": self, "request": request}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save(vacancy=vacancy)
        return response.Response(status=status.HTTP_201_CREATED)


class RespondViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    """Создание, просмотр и изменение откликов на вакансии."""

    permission_classes = (RespondPermission,)
    http_method_names = ["get", "post", "patch"]

    def get_queryset(self):
        vacancy_id = self.kwargs.get("pk")
        return get_vacancy_responds(vacancy_id=vacancy_id)

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return ser.GetRespondSerializer
        return ser.UnsafeRespondSerializer

    def perform_create(self, serializer):
        serializer.save(applicant=self.request.user.applicant)
