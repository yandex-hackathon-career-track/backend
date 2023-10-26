from rest_framework import serializers

from apps.students.models import Applicant, ApplicantCourse
from apps.api.v1.attributes.serializers import (
    JobSerializer,
    StackSerializer,
    ContactSerializer,
    WorkFormatSerializer,
)


class ApplicantCourseSerializer(serializers.ModelSerializer):
    """Сериализатор для отображения курсов соискателя."""

    course = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = ApplicantCourse
        fields = ("id", "applicant", "course", "graduation_date")


class ApplicantSerializer(serializers.ModelSerializer):
    """Сериализатор для отображения анкеты соискателя."""

    city = serializers.StringRelatedField(read_only=True)
    jobs = JobSerializer(many=True)
    stack = StackSerializer(many=True)
    work_format = WorkFormatSerializer()
    contact = ContactSerializer()
    courses = ApplicantCourseSerializer(many=True, read_only=True)

    class Meta:
        model = Applicant
        fields = (
            "id",
            "user",
            "first_name",
            "last_name",
            "total_experience",
            "can_relocate",
            "jobs",
            "stack",
            "city",
            "contact",
            "status",
            "total_experience",
            "work_format",
            "courses",
        )


class ApplicantsListSerializer(serializers.ModelSerializer):
    course = ApplicantCourseSerializer(
        many=True, read_only=True, source="applicant_courses"
    )

    stack = StackSerializer(many=True)

    class Meta:
        model = Applicant
        fields = (
            "id",
            "first_name",
            "last_name",
            "stack",
            "course",
            "status",
            "total_experience",
        )
