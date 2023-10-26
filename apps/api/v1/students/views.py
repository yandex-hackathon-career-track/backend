from rest_framework import viewsets

from apps.students.selectors import get_all_applicants
from apps.api.v1.students.serializers import ApplicantSerializer, ApplicantsListSerializer


class ApplicantViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = get_all_applicants()

    def get_serializer_class(self):
        if self.action == "list":
            return ApplicantsListSerializer
        else:
            return ApplicantSerializer
