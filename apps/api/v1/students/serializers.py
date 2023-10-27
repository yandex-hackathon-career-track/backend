from rest_framework import serializers

from apps.students.models import Applicant, ApplicantCourse
from apps.api.v1.attributes.serializers import (
    ActivityStatusSerializer,
    CourseSerializer,
    EducationSerializer,
    PortfolioLinkSerializer,
    JobSerializer,
    StackSerializer,
    ContactSerializer,
    WorkFormatSerializer,
)


class ApplicantCourseSerializer(serializers.ModelSerializer):
    """Сериализатор для отображения курсов соискателя."""

    course = CourseSerializer()
    name = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = ApplicantCourse
        fields = ("id", "name", "applicant", "course", "graduation_date")


class ApplicantSerializer(serializers.ModelSerializer):
    """Сериализатор для отображения анкеты соискателя."""

    city = serializers.StringRelatedField(read_only=True)
    jobs = JobSerializer(many=True)
    stack = StackSerializer(many=True)
    work_format = WorkFormatSerializer()
    contact = ContactSerializer()
    applicant_courses = ApplicantCourseSerializer(many=True, read_only=True)
    status = ActivityStatusSerializer()
    portfolio_links = PortfolioLinkSerializer(many=True, read_only=True)
    educations = EducationSerializer(many=True, read_only=True)
    course_directions = CourseSerializer(many=True, read_only=True)

    class Meta:
        model = Applicant
        fields = (
            "id",
            "user",
            "first_name",
            "last_name",
            "jobs",
            "stack",
            "city",
            "contact",
            "status",
            "total_experience",
            "work_format",
            "applicant_courses",
            "portfolio_links",
            "educations",
            "course_directions",
        )


class ApplicantsListSerializer(serializers.ModelSerializer):
    """Сериализатор для отображения списка соискателей."""
    status = ActivityStatusSerializer()
    stack = StackSerializer(many=True)

    class Meta:
        model = Applicant
        fields = (
            "id",
            "first_name",
            "last_name",
            "stack",
            "status",
            "total_experience",
        )

    def to_representation(self, instance):
        data = super().to_representation(instance)
        applicant_courses = instance.applicant_courses.all()
        data["applicant_courses"] = [
            {"id": course.course.id, "name": course.course.name}
            for course in applicant_courses
        ]
        return data
