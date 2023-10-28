from django.urls import include, path
from rest_framework import routers

from .attributes import views
from .employers.views import EmployerView
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
router.register("review_status", views.ReviewViewset, basename="review_status")
router.register("directions", views.DirectionViewset, basename="directions")
router.register("cources", views.CourseViewset, basename="courses")
router.register("stack", views.StackViewset, basename="stack")
router.register(
    "work_formats", views.WorkFormatViewset, basename="work_formats"
)
router.register("occupations", views.OccupationViewset, basename="occupations")
router.register("cities", views.CityViewset, basename="cities")
router.register("activity", views.ActivityStatusViewset, basename="activity")


urlpatterns = [
    path("auth/", include("djoser.urls.jwt")),
    # ЛК работодателя
    path("employers/me/", EmployerView.as_view(), name="employer_profile"),
    # Просмотр и изменение откликов на вакансии
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
    # Роутеры
    path("", include(router.urls)),
]
