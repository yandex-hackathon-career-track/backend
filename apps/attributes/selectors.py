from .models import (
    ActivityStatus,
    City,
    Course,
    Direction,
    EmployeesNumber,
    ReviewStatus,
    Stack,
    WorkFormat,
    Occupation,
)


def get_atrributes() -> dict:
    return {
        "directions": Direction.objects.all(),
        "cources": Course.objects.select_related("direction"),
        "stack": Stack.objects.all(),
        "work_formats": WorkFormat.objects.all(),
        "occupations": Occupation.objects.all(),
        "cities": City.objects.all(),
        "activity_statuses": ActivityStatus.objects.all(),
        "review_statuses": ReviewStatus.objects.all(),
        "employees_number": EmployeesNumber.objects.all(),
    }
