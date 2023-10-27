from rest_framework import generics

from ..permissions import IsEmployer
from .serializers import EmployerSerializer


class EmployerView(generics.RetrieveUpdateAPIView):
    """Чтение/измение данных профиля Работодателя в ЛК."""

    serializer_class = EmployerSerializer
    permission_classes = (IsEmployer,)
    http_method_names = ["get", "patch"]

    def get_object(self):
        return self.request.user.employer
