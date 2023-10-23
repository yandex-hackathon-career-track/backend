from rest_framework import generics, viewsets

from apps.employers.selectors import get_all_companies

from ..permissions import IsEmployerOrReadOnly
from .serializers import CompanySerializer, EmployerSerializer


class CompanyViewset(viewsets.ModelViewSet):
    serializer_class = CompanySerializer
    queryset = get_all_companies()


class EmployerView(generics.RetrieveUpdateAPIView):
    serializer_class = EmployerSerializer
    permission_classes = (IsEmployerOrReadOnly,)
    http_method_names = ["get", "put"]

    def get_object(self):
        return self.request.user.employer
