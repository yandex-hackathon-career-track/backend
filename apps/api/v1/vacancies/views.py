from rest_framework import viewsets

from apps.vacancies.selectors import get_all_vacancies

from ..permissions import IsEmployerOrReadOnly
from .serializers import VacancySerializer


class VacancyViewset(viewsets.ModelViewSet):
    """Просмотр, создание, изменение, удаление вакансий."""

    queryset = get_all_vacancies()
    serializer_class = VacancySerializer
    permission_classes = (IsEmployerOrReadOnly,)
    http_method_names = ["get", "post", "patch", "delete"]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user.employer)
