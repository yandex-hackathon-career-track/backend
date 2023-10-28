from django.contrib import admin

from .models import Employer, SelectedResume


class SelectedResumeAdmin(admin.TabularInline):
    model = SelectedResume


@admin.register(Employer)
class EmployerAdmin(admin.ModelAdmin):
    list_display = ("user", "name", "phone", "email", "selected_resumes")
    inlines = (SelectedResumeAdmin,)
    empty_value_display = "-пусто-"

    def selected_resumes(self, obj):
        return obj.selected_resumes.count()

    selected_resumes.short_description = "Избранные"
