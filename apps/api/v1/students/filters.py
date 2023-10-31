from datetime import date, timedelta

import django_filters
from django.db.models import Min, OuterRef, Subquery
from django_filters.filters import NumberFilter

from apps.attributes.models import (
    ActivityStatus,
    City,
    Course,
    Direction,
    Occupation,
    Stack,
    WorkFormat,
)
from apps.students.models import Applicant, Job


class ApplicantFilter(django_filters.FilterSet):
    start_date_experience_min = NumberFilter(
        field_name="jobs__start_date",
        method="filter_start_date_experience_min",
        label="Минимальный опыт работы (в годах)",
    )
    stack = django_filters.ModelMultipleChoiceFilter(
        queryset=Stack.objects.all(),
        field_name="stack__name",
        to_field_name="name",
        label="Stack",
        conjoined=True,
    )
    city = django_filters.ModelMultipleChoiceFilter(
        queryset=City.objects.all(),
        field_name="city__name",
        to_field_name="name",
        label="City",
        conjoined=True,
    )

    work_format = django_filters.ModelMultipleChoiceFilter(
        queryset=WorkFormat.objects.all(),
        field_name="work_format__name",
        to_field_name="name",
        label="Work Format",
        conjoined=True,
    )

    course = django_filters.ModelMultipleChoiceFilter(
        queryset=Course.objects.all(),
        field_name="applicant_courses__course__name",
        to_field_name="name",
        label="Course",
        conjoined=True,
    )

    direction = django_filters.ModelMultipleChoiceFilter(
        queryset=Direction.objects.all(),
        field_name="applicant_courses__course__direction__name",
        to_field_name="name",
        label="Direction",
        conjoined=True,
    )

    status = django_filters.ModelMultipleChoiceFilter(
        queryset=ActivityStatus.objects.all(),
        field_name="status__name",
        to_field_name="name",
        label="Status",
        conjoined=True,
    )

    occupation = django_filters.ModelMultipleChoiceFilter(
        queryset=Occupation.objects.all(),
        field_name="occupation__name",
        to_field_name="name",
        label="Occupation",
        conjoined=True,
    )
    is_selected = django_filters.BooleanFilter()

    def filter_start_date_experience_min(self, queryset, name, value):
        """
        Фильтрует соискателей по минимальному опыту работы (в годах).
        """
        years_of_experience = int(value)
        job_experience_subquery = Job.objects.filter(applicant=OuterRef("pk"))
        job_experience_subquery = job_experience_subquery.values("applicant")
        job_experience_subquery = job_experience_subquery.annotate(
            min_start_date=Min("start_date")
        )

        queryset = queryset.annotate(
            min_start_date=Subquery(
                job_experience_subquery.values("min_start_date")
            )
        )
        queryset = queryset.filter(
            min_start_date__lte=date.today()
            - timedelta(days=365 * years_of_experience)
        )
        return queryset

    class Meta:
        model = Applicant
        fields = [
            "stack",
            "city",
            "work_format",
            "direction",
            "status",
            "occupation",
            "is_selected",
        ]
        order_by = [
            ("-graduation_date", "сортировка по дате окончания обучения"),
            ("-created_at", "сортировка по дате создания"),
            ("-updated_at", "сортировка по дате обновления"),
        ]
