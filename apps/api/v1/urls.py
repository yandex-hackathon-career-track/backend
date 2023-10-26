from django.urls import include, path
from rest_framework import routers

from .employers.views import CandidateStatusViewset, EmployerView
from .users.views import UserViewSet
from .vacancies.views import RespondViewSet, VacancyViewset

app_name = "api"

router = routers.DefaultRouter()
router.register("users", UserViewSet, basename="users")
router.register("vacancies", VacancyViewset, basename="vacancies")
router.register(
    "vacancies/<uuid:pk>/responds", RespondViewSet, basename="responds"
)
router.register("candidate_status", CandidateStatusViewset, basename="")
router.register("applicants", UserViewSet, basename="applicants")


urlpatterns = [
    path("auth/", include("djoser.urls.jwt")),
    path("employers/me/", EmployerView.as_view(), name="employer_profile"),
    path("", include(router.urls)),
]
