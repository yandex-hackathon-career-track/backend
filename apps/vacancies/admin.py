from django.contrib import admin

from .models import Respond, Vacancy


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ("creator", "title", "is_published")
    empty_value_display = "-пусто-"


@admin.register(Respond)
class RespondAdmin(admin.ModelAdmin):
    list_display = ("applicant", "vacancy", "status")
    empty_value_display = "-пусто-"
