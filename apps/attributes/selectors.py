from .models import ReviewStatus


def get_all_review_statuses():
    return ReviewStatus.objects.all()
