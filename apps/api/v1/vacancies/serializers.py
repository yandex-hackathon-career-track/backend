from rest_framework import serializers

from apps.students.models import Applicant
from apps.vacancies.models import Respond, Vacancy
from apps.vacancies.selectors import (
    already_responded,
    get_vacancy_with_responds,
    same_titled_vacancy_exists,
)

from ..attributes.serializers import (
    CitySerializer,
    OccupationSerializer,
    ReviewStatusSerializer,
    WorkFormatSerializer,
)
from ..employers.serializers import EmployerSerializer


class BaseVacancySerializer(serializers.ModelSerializer):
    """Базовый сериализатор для вакансий работодателя."""

    is_published = serializers.BooleanField(required=False)

    class Meta:
        fields = ("id", "title", "is_published", "created_at", "updated_at")
        model = Vacancy
        read_only_fields = ("created_at", "updated_at")


class UnsafeVacancySerializer(BaseVacancySerializer):
    """Сериализация создания/изменения полей вакансий в ЛК работодателя."""

    is_published = serializers.BooleanField(required=False)

    class Meta(BaseVacancySerializer.Meta):
        fields = BaseVacancySerializer.Meta.fields + (
            "attendance",
            "occupation",
            "description",
            "min_salary",
            "max_salary",
            "city",
        )

    def validate(self, data):
        employer = self.context.get("request").user.employer
        if not employer.name or not (employer.email or employer.phone):
            raise serializers.ValidationError(
                "Необходимо заполнить профиль перед публикацией вакансии."
            )
        title = data.get("title")
        if title and same_titled_vacancy_exists(
            title, employer, self.instance
        ):
            raise serializers.ValidationError(
                "Уже есть вакансия на такую должность."
            )
        return super().validate(data)


class ListVacancySerializer(BaseVacancySerializer):
    """Сериализация для списка вакансий в ЛК работодателя."""

    views_qty = serializers.IntegerField()
    responds_qty = serializers.IntegerField()
    total_resume_qty = serializers.IntegerField()
    chosen_resume_qty = serializers.IntegerField()

    class Meta(BaseVacancySerializer.Meta):
        fields = BaseVacancySerializer.Meta.fields + (
            "views_qty",
            "responds_qty",
            "total_resume_qty",
            "chosen_resume_qty",
        )


class DetailMyVacancySerializer(BaseVacancySerializer):
    """Сериализация для 1 вакансии работодателя (для изменения)."""

    attendance = WorkFormatSerializer()
    occupation = OccupationSerializer()
    city = CitySerializer()

    class Meta(BaseVacancySerializer.Meta):
        fields = BaseVacancySerializer.Meta.fields + (
            "attendance",
            "occupation",
            "description",
            "min_salary",
            "max_salary",
            "city",
        )
        model = Vacancy


class DetailVacancySerializer(BaseVacancySerializer):
    """Сериализация для 1 вакансии работодателя (для просмотра)."""

    creator = EmployerSerializer()
    attendance = WorkFormatSerializer()
    occupation = OccupationSerializer()
    city = CitySerializer()

    class Meta(BaseVacancySerializer.Meta):
        fields = BaseVacancySerializer.Meta.fields + (
            "creator",
            "attendance",
            "occupation",
            "description",
            "min_salary",
            "max_salary",
            "city",
        )
        model = Vacancy


class ApplicantInRespondSerializer(serializers.ModelSerializer):
    """Сериализация полей соискателя."""

    email = serializers.EmailField(source="contact.email")
    telegram = serializers.CharField(source="contact.telegram")

    class Meta:
        fields = ("id", "first_name", "last_name", "email", "telegram")
        model = Applicant


class BaseRespondSerializer(serializers.ModelSerializer):
    """Базовый сериализатор для откликов."""

    class Meta:
        fields = ("id", "applicant")
        model = Respond


class CreateRespondSerializer(BaseRespondSerializer):
    """Сериализатор для создания откликов."""

    def validate(self, data):
        vacancy_id = self.context.get("view").kwargs.get("pk")
        if already_responded(
            vacancy_id=vacancy_id, applicant=data.get("applicant")
        ):
            raise serializers.ValidationError(
                "Откликнуться можно только 1 раз."
            )
        return super().validate(data)


class EditRespondSerializer(BaseRespondSerializer):
    """Сериализатор для Изменения статуса отклика."""

    class Meta(BaseRespondSerializer.Meta):
        fields = BaseRespondSerializer.Meta.fields + ("status",)
        read_only_fields = ("applicant",)


class NewRespondsStatSerializer(serializers.ModelSerializer):
    new = serializers.IntegerField()
    under_review = serializers.IntegerField()
    sent_test = serializers.IntegerField()
    interview = serializers.IntegerField()
    refusal = serializers.IntegerField()

    class Meta:
        model = Vacancy
        fields = (
            "new",
            "under_review",
            "sent_test",
            "interview",
            "refusal",
        )


class UpdatedRespondSerializer(BaseRespondSerializer):
    """Сериализатор для ответа после изменения статуса отклика."""

    status = serializers.CharField(source="status.name")
    vacancy_new_stats = serializers.SerializerMethodField()

    class Meta(BaseRespondSerializer.Meta):
        fields = BaseRespondSerializer.Meta.fields + (
            "status",
            "vacancy_new_stats",
        )
        read_only_fields = ("applicant",)

    def get_vacancy_new_stats(self, obj):
        vacancy = get_vacancy_with_responds(
            vacancy_id=obj.vacancy.id, prefetch_required=False
        )
        return NewRespondsStatSerializer(instance=vacancy).data


class GetRespondSerializer(BaseRespondSerializer):
    """Сериализатор для получения списка откликов."""

    applicant = ApplicantInRespondSerializer()
    status = ReviewStatusSerializer()

    class Meta(BaseRespondSerializer.Meta):
        fields = BaseRespondSerializer.Meta.fields + ("status",)


class VacancyWithRespondsSerializer(serializers.ModelSerializer):
    """Сериализация списка откликов и статистики."""

    responds = GetRespondSerializer(many=True)
    new = serializers.IntegerField()
    under_review = serializers.IntegerField()
    sent_test = serializers.IntegerField()
    interview = serializers.IntegerField()
    refusal = serializers.IntegerField()

    class Meta:
        model = Vacancy
        fields = (
            "id",
            "new",
            "under_review",
            "sent_test",
            "interview",
            "refusal",
            "responds",
        )
