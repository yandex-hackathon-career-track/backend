from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.decorators import action

from apps.api.v1.permissions import IsEmployer
from apps.students.selectors import get_all_applicants
from apps.api.v1.students.serializers import (
    ApplicantSerializer,
    ApplicantsListSerializer,
)
from .filters import ApplicantFilter

from apps.students.services import render_response_with_report


class ApplicantViewSet(viewsets.ReadOnlyModelViewSet):
    """Просмотр и отбор соискателей."""

    filter_backends = [DjangoFilterBackend]
    filterset_class = ApplicantFilter
    permission_classes = (IsEmployer,)

    def get_serializer_class(self):
        if self.action == "list":
            return ApplicantsListSerializer
        return ApplicantSerializer

    def get_queryset(self):
        return get_all_applicants(user=self.request.user)

    @action(detail=False)
    def download_report(self, request):
        """Скачать список отобранных соискателей."""
        applicants = self.filter_queryset(self.get_queryset())
        return render_response_with_report(applicants=applicants)
