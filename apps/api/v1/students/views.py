from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.decorators import action

from apps.api.v1.permissions import IsEmployer
from apps.api.v1.students.serializers import (
    ApplicantSerializer,
    ApplicantsListSerializer,
)
from apps.core.utils import generate_pdf
from apps.students.selectors import get_all_applicants
from apps.students.services import render_response_with_report

from .filters import ApplicantFilter


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

    @action(detail=True)
    def generate_pdf(self, request, pk=None):
        applicant = self.get_object()
        applicant_serializer = ApplicantSerializer(applicant)
        response = generate_pdf(applicant, applicant_serializer)
        return response
