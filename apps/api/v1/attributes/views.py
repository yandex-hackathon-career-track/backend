from rest_framework import viewsets

from apps.attributes import selectors

from . import serializers


class ReviewViewset(viewsets.ReadOnlyModelViewSet):
    """Просмотр статусов рассмотрения откликов/резюме."""

    queryset = selectors.get_all_review_statuses()
    serializer_class = serializers.ReviewStatusSerializer
