from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


@admin.register(CustomUser)
class MyUserAdmin(UserAdmin):
    fieldsets = (
        ("Основные поля", {"fields": ("email", "password", "role")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        ("Важные даты", {"fields": ("last_login",)}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2", "role"),
            },
        ),
    )
    list_display = ("id", "email", "role", "is_active")
    empty_value_display = "-пусто-"
    ordering = ("email",)


# @admin.register(CustomUser)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ("id", "email", "role", "is_active")
#     empty_value_display = "-пусто-"
