from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, views, decorators, status
from rest_framework.response import Response

from apps.vacancies.models import Vacancy
from apps.vacancies.selectors import (
    get_published_vacancies,
    get_employer_vacancies_by_user,
    get_respond_by_id,
    get_vacancy_with_responds,
)

from ..permissions import (
    IsApplicant,
    IsEmployer,
    IsEmployerCreator,
)
from . import serializers as ser


class MyVacancyViewset(viewsets.ModelViewSet):
    """Просмотр, создание, изменение вакансий."""

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
        """Создание отклика на вакансию."""
        vacancy = get_object_or_404(Vacancy, id=pk)
        serializer = ser.CreateRespondSerializer(
            data=request.data, context={"view": self, "request": request}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save(vacancy=vacancy)
        return Response(status=status.HTTP_201_CREATED)


class GetRespondsView(views.APIView):
    """Получение списка откликов на вакансию."""

    permission_classes = (IsEmployerCreator,)

    @extend_schema(responses=ser.VacancyWithRespondsSerializer)
    def get(self, request, pk):
        vacancy = get_vacancy_with_responds(pk)
        serializer = ser.VacancyWithRespondsSerializer(instance=vacancy)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UpdateRespondStatusView(views.APIView):
    """Изменение статуса отклика на вакансию."""

    permission_classes = (IsEmployerCreator,)

    @extend_schema(
        request=ser.EditRespondSerializer, responses=ser.EditRespondSerializer
    )
    def patch(self, request, pk, respond_id):
        respond = get_respond_by_id(vacancy_id=pk, respond_id=respond_id)
        serializer = ser.EditRespondSerializer(
            instance=respond, data=request.data
        )
        serializer.is_valid(raise_exception=True)
        respond = serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
