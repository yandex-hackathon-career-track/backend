from rest_framework import viewsets

from apps.attributes.models import (
    ActivityStatus,
    City,
    Course,
    Direction,
    Occupation,
    ReviewStatus,
    Stack,
    WorkFormat,
)

from . import serializers


class DirectionViewset(viewsets.ReadOnlyModelViewSet):
    """Просмотр направлений курсов."""

    queryset = Direction.objects.all()
    serializer_class = serializers.ReviewStatusSerializer


class CourseViewset(viewsets.ReadOnlyModelViewSet):
    """Просмотр статусов рассмотрения откликов/резюме."""

    queryset = Course.objects.all()
    serializer_class = serializers.CourseSerializer


class StackViewset(viewsets.ReadOnlyModelViewSet):
    """Просмотр стека инструментов."""

    queryset = Stack.objects.all()
    serializer_class = serializers.StackSerializer


class WorkFormatViewset(viewsets.ReadOnlyModelViewSet):
    """Просмотр форматов работы."""

    queryset = WorkFormat.objects.all()
    serializer_class = serializers.WorkFormatSerializer


class OccupationViewset(viewsets.ReadOnlyModelViewSet):
    """Просмотр типов занятости."""

    queryset = Occupation.objects.all()
    serializer_class = serializers.OccupationSerializer


class CityViewset(viewsets.ReadOnlyModelViewSet):
    """Просмотр городов."""

    queryset = City.objects.all()
    serializer_class = serializers.CitySerializer


class ActivityStatusViewset(viewsets.ReadOnlyModelViewSet):
    """Просмотр статусов активности студентов."""

    queryset = ActivityStatus.objects.all()
    serializer_class = serializers.ActivityStatusSerializer


class ReviewViewset(viewsets.ReadOnlyModelViewSet):
    """Просмотр статусов рассмотрения откликов/резюме."""

    queryset = ReviewStatus.objects.all()
    serializer_class = serializers.ReviewStatusSerializer
