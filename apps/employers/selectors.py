from .models import CandidateStatus


def get_all_candidate_statuses():
    return CandidateStatus.objects.all()
