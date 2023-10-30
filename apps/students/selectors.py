from django.db.models import Q, Exists, OuterRef

from apps.students.models import Applicant


def create_filter(values, field_name):
    filter = Q()
    filter |= Q(**{field_name + "__in": values})
    return filter


def get_all_applicants(user, filters={}):
    queryset = (
        Applicant.objects.select_related("city", "status")
        .prefetch_related(
            "stack",
            "applicant_courses__course__direction",
            "educations",
            "portfolio_links",
            "work_format",
            "occupation",
        )
        .annotate(
            is_selected=Exists(
                user.employer.selected_resumes.filter(
                    applicant__pk=OuterRef("pk")
                )
            )
        )
    )

    for field, values in filters.items():
        if values:
            filter = create_filter(values, field)
            queryset = queryset.filter(filter)

    return queryset
