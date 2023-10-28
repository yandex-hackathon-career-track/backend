from django.contrib import admin

from .models import Applicant


@admin.register(Applicant)
class ApplicantAdmin(admin.ModelAdmin):
    list_display = ("user", "first_name", "last_name", "status")
    empty_value_display = "-пусто-"
