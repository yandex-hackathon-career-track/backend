from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated

from apps.employers.selectors import get_all_companies

from ..permissions import IsEmployerOrReadOnly
from .serializers import CompanySerializer, EmployerSerializer


class CompanyViewset(viewsets.ModelViewSet):
    serializer_class = CompanySerializer
    permission_classes = (IsEmployerOrReadOnly,)
    queryset = get_all_companies()


class EmployerView(generics.RetrieveUpdateAPIView):
    """Чтение/измение данных профиля Работодателя в ЛК."""

    serializer_class = EmployerSerializer
    permission_classes = (IsAuthenticated,)
    http_method_names = ["get", "patch"]

    def get_object(self):
        return self.request.user.employer
