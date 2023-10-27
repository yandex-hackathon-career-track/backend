from django.urls import include, path
from rest_framework import routers

from .attributes import views
from .employers.views import EmployerView
from .users.views import UserViewSet
from .vacancies.views import RespondViewSet, MyVacancyViewset, VacancyViewset

app_name = "api"

router = routers.DefaultRouter()
router.register("users", UserViewSet, basename="users")
router.register(
    "employers/vacancies", MyVacancyViewset, basename="my_vacancies"
)
router.register(
    "employers/vacancies/<uuid:pk>/responds",
    RespondViewSet,
    basename="responds",
)
router.register("vacancies", VacancyViewset, basename="vacancies")
# тут что-то не так - используется Userviewset
# router.register("applicants", UserViewSet, basename="applicants")
router.register("review_status", views.ReviewViewset, basename="review_status")


urlpatterns = [
    path("auth/", include("djoser.urls.jwt")),
    path("employers/me/", EmployerView.as_view(), name="employer_profile"),
    path("", include(router.urls)),
]
