from rest_framework import viewsets

from apps.students.selectors import get_all_applicants
from apps.api.v1.students.serializers import ApplicantSerializer

class ApplicantViewSet(viewsets.ModelViewSet):
    queryset = get_all_applicants()
    serializer_class = ApplicantSerializer