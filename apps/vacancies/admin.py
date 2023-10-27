from django.contrib import admin

from .models import Vacancy


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ("creator", "title", "is_published")
    empty_value_display = "-пусто-"
