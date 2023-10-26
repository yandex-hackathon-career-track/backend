from rest_framework import generics, viewsets

from apps.employers.selectors import get_all_candidate_statuses

from .serializers import CandidateStatusSerializer, EmployerSerializer


class EmployerView(generics.RetrieveUpdateAPIView):
    """Чтение/измение данных профиля Работодателя в ЛК."""

    serializer_class = EmployerSerializer
    # permission_classes = (IsAuthenticated,)
    http_method_names = ["get", "patch"]

    def get_object(self):
        return self.request.user.employer


class CandidateStatusViewset(viewsets.ReadOnlyModelViewSet):
    """Просмотр доступных статусов кандидатов."""

    queryset = get_all_candidate_statuses()
    serializer_class = CandidateStatusSerializer
