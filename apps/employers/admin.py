from django.contrib import admin

from .models import Company, Employer


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    pass


@admin.register(Employer)
class EmployerAdmin(admin.ModelAdmin):
    pass
