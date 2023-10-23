from django.urls import include, path
from rest_framework import routers

from .employers.views import CompanyViewset, EmployerView
from .users.views import UserViewSet

app_name = "users"

router = routers.DefaultRouter()
router.register("users", UserViewSet, basename="users")
router.register("companies", CompanyViewset, basename="companies")

urlpatterns = [
    path("auth/", include("djoser.urls.jwt")),
    path("employers/me/", EmployerView.as_view(), name="employer_profile"),
    path("", include(router.urls)),
]
