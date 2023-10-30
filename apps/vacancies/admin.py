from django.contrib import admin

from .models import Respond, Vacancy


class RespondAdmin(admin.TabularInline):
    model = Respond


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ("creator", "title", "is_published", "responds")
    inlines = (RespondAdmin,)
    empty_value_display = "-пусто-"

    def responds(self, obj):
        return obj.responds.count()

    responds.short_description = "Откликов"
