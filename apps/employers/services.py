from .models import Employer


def create_employer(user) -> Employer:
    return Employer.objects.create(user=user)
