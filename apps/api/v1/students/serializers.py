from rest_framework import serializers
from apps.students.models import Applicant

class ApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicant
        fields = (
            'id',
            'user',
            'photo',
            'first_name',
            'last_name',
            'exp_start',
            'birthday',
            'can_relocate',
            'portfolio_link',
            'direction',
            'stack',
            'city',
            'contact',
            'status',
            'education_level',
            'work_format',
            'experience',
            'age',
        )