from djoser.views import UserViewSet as DjoserViewSet
from drf_spectacular.utils import extend_schema
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status


class UserViewSet(DjoserViewSet):
    """Создание пользователя/получение данных о пользователе."""

    @action(["get"], detail=False)
    def me(self, request, *args, **kwargs):
        """
        Общая информация о пользователе: id, email, role.
        Возможные роли: employer/applicant/admin.
        """
        serializer = self.get_serializer_class()
        return Response(
            serializer(request.user).data, status=status.HTTP_200_OK
        )

    # отключаем смену логина (email)
    @extend_schema(exclude=True)
    def reset_username(self, request, *args, **kwargs):
        pass

    @extend_schema(exclude=True)
    def reset_username_confirm(self, request, *args, **kwargs):
        pass

    # отключаем установку логина (email)
    @extend_schema(exclude=True)
    def set_username(self, request, *args, **kwargs):
        pass

    # отключаем отправку активации
    @extend_schema(exclude=True)
    def activation(self, request, *args, **kwargs):
        pass

    # отключаем повторную отправку активации
    @extend_schema(exclude=True)
    def resend_activation(self, request, *args, **kwargs):
        pass

    # отключаем ручки list/retrieve/update/partial_update/destroy
    @extend_schema(exclude=True)
    def list(self, request, *args, **kwargs):
        pass

    @extend_schema(exclude=True)
    def retrieve(self, request, *args, **kwargs):
        pass

    @extend_schema(exclude=True)
    def update(self, request, *args, **kwargs):
        pass

    @extend_schema(exclude=True)
    def partial_update(self, request, *args, **kwargs):
        pass

    @extend_schema(exclude=True)
    def destroy(self, request, *args, **kwargs):
        pass
