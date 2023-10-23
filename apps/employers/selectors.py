from .models import Company


def get_all_companies():
    return Company.objects.all()
