from django.urls import include, path
from rest_framework import routers

from .attributes.views import AttributesView
from .employers.views import EmployerView, SelectedResumeView
from .users.views import UserViewSet
from .vacancies.views import (
    MyVacancyViewset,
    VacancyViewset,
    GetRespondsView,
    UpdateRespondStatusView,
)
from .students.views import ApplicantViewSet

app_name = "api"

router = routers.DefaultRouter()
router.register("users", UserViewSet, basename="users")
router.register(
    "employers/vacancies", MyVacancyViewset, basename="my_vacancies"
)
router.register("vacancies", VacancyViewset, basename="vacancies")
router.register("applicants", ApplicantViewSet, basename="applicants")
# router.register(
#     "applicants/<uuid:id>/selected", SelectedResumeView, basename="selected"
# )


urlpatterns = [
    path("auth/", include("djoser.urls.jwt")),
    path(
        "applicants/<uuid:id>/selected/",
        SelectedResumeView.as_view(),
        name="selected",
    ),
    path("attributes/", AttributesView.as_view(), name="attributes"),
    path("employers/me/", EmployerView.as_view(), name="employer_profile"),
    path(
        "employers/vacancies/<uuid:pk>/responds/",
        GetRespondsView.as_view(),
        name="vacancy_responds",
    ),
    path(
        "employers/vacancies/<uuid:pk>/responds/<int:respond_id>/",
        UpdateRespondStatusView.as_view(),
        name="update_respond_status",
    ),
    path("", include(router.urls)),
]
