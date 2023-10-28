from django.contrib import admin

from .models import Applicant, ApplicantCourse, Job, Education, PortfolioLink


class EmployeeAdmin(admin.TabularInline):
    model = ApplicantCourse


class JobAdmin(admin.TabularInline):
    model = Job


class EducationAdmin(admin.TabularInline):
    model = Education


class PortfolioAdmin(admin.TabularInline):
    model = PortfolioLink


@admin.register(Applicant)
class ApplicantAdmin(admin.ModelAdmin):
    inlines = (EmployeeAdmin, JobAdmin, EducationAdmin, PortfolioAdmin)
    list_display = ("user", "first_name", "last_name", "status")
    autocomplete_fields = ("stack", "work_format", "occupation")
    empty_value_display = "-пусто-"
