from apps.students.models import Applicant


def get_all_applicants():
    return Applicant.objects.all()
