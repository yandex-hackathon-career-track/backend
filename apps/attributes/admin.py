from django.contrib import admin

from .models import (
    ActivityStatus,
    City,
    Course,
    Direction,
    ReviewStatus,
    Stack,
    WorkFormat,
    Occupation,
)


@admin.register(ActivityStatus)
class ActivityStatusAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    empty_value_display = "-пусто-"


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    empty_value_display = "-пусто-"


@admin.register(Direction)
class DirectionAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    empty_value_display = "-пусто-"


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "direction")
    empty_value_display = "-пусто-"


@admin.register(ReviewStatus)
class ReviewStatusAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    empty_value_display = "-пусто-"


@admin.register(Stack)
class StackAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    empty_value_display = "-пусто-"


@admin.register(WorkFormat)
class WorkFormatAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    empty_value_display = "-пусто-"


@admin.register(Occupation)
class OccupationAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    empty_value_display = "-пусто-"
