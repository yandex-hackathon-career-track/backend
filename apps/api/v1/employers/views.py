from rest_framework import generics, viewsets

from apps.employers.selectors import get_selected_relation

from ..permissions import IsEmployer
from .serializers import EmployerSerializer, SelectedResumeSerializer


class EmployerView(generics.RetrieveUpdateAPIView):
    """Чтение/измение данных профиля Работодателя в ЛК."""

    serializer_class = EmployerSerializer
    permission_classes = (IsEmployer,)
    http_method_names = ["get", "patch"]

    def get_object(self):
        return self.request.user.employer


class SelectedResumeView(viewsets.ModelViewSet):
    serializer_class = SelectedResumeSerializer
    permission_classes = (IsEmployer,)
    http_method_names = ["post", "patch", "delete"]

    def get_object(self):
        applicant_id = self.kwargs.get("id")
        employer = self.request.employer
        return get_selected_relation(employer, applicant_id)
