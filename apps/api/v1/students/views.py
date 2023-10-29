import pandas as pd

from django_filters.rest_framework import DjangoFilterBackend
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.decorators import action

from apps.api.v1.permissions import IsEmployer
from apps.students.selectors import get_all_applicants
from apps.api.v1.students.serializers import (
    ApplicantSerializer,
    ApplicantsListSerializer,
)
from .filters import ApplicantFilter

from apps.students.services import get_dataframe


class ApplicantViewSet(viewsets.ReadOnlyModelViewSet):
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
        applicants = self.filter_queryset(self.get_queryset())
        dataframe = get_dataframe(applicants)

        filename = "applicants.xlsx"
        response = HttpResponse(content_type="application/vnd.ms-excel")
        response["Content-Disposition"] = f"attachment; filename={filename}"

        with pd.ExcelWriter(response, engine="xlsxwriter") as writer:
            dataframe.to_excel(writer, sheet_name="applicants", index=False)
            workbook = writer.book
            worksheet = writer.sheets["applicants"]
            worksheet.set_zoom(90)
            workbook.add_format({"align": "right", "bold": True, "bottom": 6})
            worksheet.set_column("A:A", 15)
            worksheet.set_column("B:C", 20)
            worksheet.set_column("D:D", 12)
            worksheet.set_column("E:E", 22)
            worksheet.set_column("F:F", 12)
            worksheet.set_column("G:H", 20)

        return response
