from rest_framework import serializers

from apps.attributes.models import (
    ActivityStatus,
    City,
    Contact,
    Course,
    Direction,
    Occupation,
    ReviewStatus,
    Stack,
    WorkFormat,
)
from apps.students.models import Education, Job, PortfolioLink


class DirectionSerializer(serializers.ModelSerializer):
    """Сериализатор для отображения направлений."""

    class Meta:
        model = Direction
        fields = ("id", "name")


class CourseSerializer(serializers.ModelSerializer):
    """Сериализатор для отображения курсов."""

    direction = DirectionSerializer()

    class Meta:
        model = Course
        fields = ("id", "name", "direction")


class PortfolioLinkSerializer(serializers.ModelSerializer):
    """Сериализатор для отображения ссылок на портфолио."""

    class Meta:
        model = PortfolioLink
        fields = ("id", "name", "link")


class JobSerializer(serializers.ModelSerializer):
    """Сериализатор для опыта работы."""

    class Meta:
        model = Job
        fields = ("id", "name", "experience")


class StackSerializer(serializers.ModelSerializer):
    """Сериализатор для отображения стека."""

    class Meta:
        model = Stack
        fields = ("id", "name")


class ContactSerializer(serializers.ModelSerializer):
    """Сериализатор для отображения контактов."""

    class Meta:
        model = Contact
        fields = ("id", "email", "telegram")


class EducationSerializer(serializers.ModelSerializer):
    """Сериализатор для отображения образования."""

    class Meta:
        model = Education
        fields = ("id", "name")


class WorkFormatSerializer(serializers.ModelSerializer):
    """Сериализатор для формата работы."""

    class Meta:
        model = WorkFormat
        fields = ("id", "name")


class ActivityStatusSerializer(serializers.ModelSerializer):
    """Сериализатор для статуса поиска."""

    class Meta:
        model = ActivityStatus
        fields = ("id", "name")


class ReviewStatusSerializer(serializers.ModelSerializer):
    """Сериализатор для статуса рассмотрения откликов/резюме."""

    class Meta:
        model = ReviewStatus
        fields = ("id", "name")


class CitySerializer(serializers.ModelSerializer):
    """Сериализатор для городов."""

    class Meta:
        model = City
        fields = ("id", "name")


class OccupationSerializer(serializers.ModelSerializer):
    """Сериализатор для типов занятости."""

    class Meta:
        model = Occupation
        fields = ("id", "name")
