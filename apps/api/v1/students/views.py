from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from apps.api.v1.permissions import IsEmployer
from apps.students.selectors import get_all_applicants
from apps.api.v1.students.serializers import (
    ApplicantSerializer,
    ApplicantsListSerializer,
)
from .filters import ApplicantFilter


class ApplicantViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = get_all_applicants()
    filter_backends = [DjangoFilterBackend]
    filterset_class = ApplicantFilter
    permission_classes = (IsEmployer,)

    def get_serializer_class(self):
        if self.action == "list":
            return ApplicantsListSerializer
        return ApplicantSerializer
