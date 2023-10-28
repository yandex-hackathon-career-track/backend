import django_filters

from apps.students.models import Applicant
from apps.attributes.models import (
    ActivityStatus,
    City,
    Course,
    Direction,
    Occupation,
    Stack,
    WorkFormat,
)


class ApplicantFilter(django_filters.FilterSet):
    stack = django_filters.ModelMultipleChoiceFilter(
        queryset=Stack.objects.all(),
        field_name="stack__name",
        to_field_name="name",
        label="Stack",
    )
    city = django_filters.ModelMultipleChoiceFilter(
        queryset=City.objects.all(),
        field_name="city__name",
        to_field_name="name",
        label="City",
    )

    work_format = django_filters.ModelMultipleChoiceFilter(
        queryset=WorkFormat.objects.all(),
        field_name="work_format__name",
        to_field_name="name",
        label="Work Format",
    )

    course = django_filters.ModelMultipleChoiceFilter(
        queryset=Course.objects.all(),
        field_name="applicant_courses__course__name",
        to_field_name="name",
        label="Course",
    )

    direction = django_filters.ModelMultipleChoiceFilter(
        queryset=Direction.objects.all(),
        field_name="applicant_courses__course__direction__name",
        to_field_name="name",
        label="Direction",
    )

    status = django_filters.ModelMultipleChoiceFilter(
        queryset=ActivityStatus.objects.all(),
        field_name="status__name",
        to_field_name="name",
        label="Status",
    )

    occupation = django_filters.ModelMultipleChoiceFilter(
        queryset=Occupation.objects.all(),
        field_name="occupation__name",
        to_field_name="name",
        label="Occupation",
    )

    class Meta:
        model = Applicant
        fields = [
            "stack",
            "city",
            "work_format",
            "direction",
            "status",
            "occupation",
        ]
        order_by = [
            ("-graduation_date", "Сортировка по дате окончания обучения"),
            ("-created_at", "Сортировка по дате создания"),
            ("-updated_at", "Сортировка по дате обновления"),
        ]
