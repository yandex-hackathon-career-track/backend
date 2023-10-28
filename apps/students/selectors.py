from django.db.models import Q

from apps.students.models import Applicant, Education, PortfolioLink
from apps.attributes.models import City, WorkFormat, Occupation

def create_filter(values, field_name):
    filter = Q()
    filter |= Q(**{field_name + "__in": values})
    return filter

def get_all_applicants(filters={}):
    queryset = Applicant.objects.select_related(
        "city", "status", "work_format", "occupation"
    ).prefetch_related(
        "stack", "applicant_courses__course__direction", "educations", "portfolio_links"
    )

    for field, values in filters.items():
        if values:
            filter = create_filter(values, field)
            queryset = queryset.filter(filter)

    return queryset