from django.contrib import admin

from .models import Employer


@admin.register(Employer)
class EmployerAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "name",
        "phone",
        "email",
    )
    empty_value_display = "-пусто-"
