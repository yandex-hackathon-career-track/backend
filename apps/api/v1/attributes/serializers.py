from rest_framework import serializers


from apps.students.models import PortfolioLink, Job, Education
from apps.attributes.models import (
    ActivityStatus,
    Direction,
    Stack,
    Contact,
    Course,
    WorkFormat,
)


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
        fields = ("id", "applicant", "name", "link")


class JobSerializer(serializers.ModelSerializer):
    """Сериализатор для опыта работы."""

    class Meta:
        model = Job
        fields = ("id", "name")


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
