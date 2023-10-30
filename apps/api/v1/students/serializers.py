from rest_framework import serializers
from django.db.models import Max

from apps.students.models import Applicant, ApplicantCourse
from apps.api.v1.attributes.serializers import (
    ActivityStatusSerializer,
    CourseSerializer,
    EducationSerializer,
    OccupationSerializer,
    PortfolioLinkSerializer,
    JobSerializer,
    StackSerializer,
    ContactSerializer,
    WorkFormatSerializer,
)


class ApplicantCourseSerializer(serializers.ModelSerializer):
    """Сериализатор для отображения курсов соискателя."""

    course = CourseSerializer()

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["course"] = instance.course.name
        return data

    class Meta:
        model = ApplicantCourse
        fields = ("id", "course", "graduation_date")


class ApplicantSerializer(serializers.ModelSerializer):
    """Сериализатор для отображения анкеты соискателя."""

    city = serializers.StringRelatedField(read_only=True)
    jobs = JobSerializer(many=True)
    stack = StackSerializer(many=True)
    work_format = WorkFormatSerializer(many=True)
    contact = ContactSerializer()
    applicant_courses = ApplicantCourseSerializer(many=True)
    status = ActivityStatusSerializer()
    portfolio_links = PortfolioLinkSerializer(many=True, read_only=True)
    educations = EducationSerializer(many=True, read_only=True)
    occupation = OccupationSerializer(many=True)
    direction = serializers.SerializerMethodField()
    is_selected = serializers.BooleanField()

    def get_direction(self, obj):
        if obj.applicant_courses.exists():
            latest_course = obj.applicant_courses.latest("graduation_date")
            direction = latest_course.course.direction
            return {"id": direction.id, "name": direction.name}
        return None

    def to_representation(self, instance):
        data = super().to_representation(instance)
        contact_data = data.get("contact")
        if contact_data:
            contact_data = {
                key: value for key, value in contact_data.items() if value
            }
            if contact_data:
                data["contact"] = contact_data
            else:
                del data["contact"]
        return data

    class Meta:
        model = Applicant
        fields = (
            "id",
            "user",
            "status",
            "first_name",
            "last_name",
            "direction",
            "total_experience",
            "jobs",
            "applicant_courses",
            "educations",
            "stack",
            "work_format",
            "occupation",
            "city",
            "portfolio_links",
            "contact",
            "updated_at",
            "is_selected",
        )


class ApplicantsListSerializer(serializers.ModelSerializer):
    """Сериализатор для отображения списка соискателей."""

    status = ActivityStatusSerializer()
    stack = StackSerializer(many=True)
    direction = serializers.SerializerMethodField()
    latest_graduation_date = serializers.SerializerMethodField()
    is_selected = serializers.BooleanField()

    def get_direction(self, obj):
        if obj.applicant_courses.exists():
            latest_course = obj.applicant_courses.latest("graduation_date")
            direction = latest_course.course.direction
            return {"id": direction.id, "name": direction.name}
        return None

    def get_latest_graduation_date(self, obj):
        if obj.applicant_courses.exists():
            latest_course = obj.applicant_courses.annotate(
                latest_graduation_date=Max("graduation_date")
            ).first()
            return latest_course.latest_graduation_date
        return None

    class Meta:
        model = Applicant
        fields = (
            "id",
            "user",
            "first_name",
            "last_name",
            "stack",
            "status",
            "total_experience",
            "direction",
            "updated_at",
            "latest_graduation_date",
            "is_selected",
        )
