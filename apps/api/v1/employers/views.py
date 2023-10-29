from django.core.exceptions import ObjectDoesNotExist
from rest_framework import generics, views, status
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser
from rest_framework.response import Response
from rest_framework.serializers import ValidationError

from apps.core.exceptions import ObjectAlreadyExistsException
from apps.employers.services import add_to_selected, remove_from_selected

from ..permissions import IsEmployer
from .serializers import (
    ReadEmployerSerializer,
    UpdateEmployerSerializer,
)


class EmployerView(generics.RetrieveUpdateAPIView):
    """Чтение/измение данных профиля Работодателя в ЛК."""

    permission_classes = (IsEmployer,)
    http_method_names = ["get", "patch"]
    parser_classes = (MultiPartParser, FormParser, JSONParser)

    def get_serializer_class(self):
        if self.request.method == "get":
            return ReadEmployerSerializer
        return UpdateEmployerSerializer

    def get_object(self):
        return self.request.user.employer


class SelectedResumeView(views.APIView):
    """Добавление/удаление соискателей из Избранного."""

    def post(self, request, id):
        """Добавление соискателя в Избранное."""
        try:
            add_to_selected(user=request.user, applicant_id=id)
        except ObjectAlreadyExistsException as e:
            raise ValidationError(e)
        return Response(status=status.HTTP_201_CREATED)

    def delete(self, request, id):
        """Удаление соискателя из Избранного."""
        try:
            remove_from_selected(user=request.user, applicant_id=id)
        except ObjectDoesNotExist as e:
            raise ValidationError(e)
        return Response(status=status.HTTP_204_NO_CONTENT)
