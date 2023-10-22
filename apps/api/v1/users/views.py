from djoser.views import UserViewSet as DjoserViewSet
from drf_spectacular.utils import extend_schema
from rest_framework.decorators import action


class UserViewSet(DjoserViewSet):
    @action(["get"], detail=False)
    def me(self, request, *args, **kwargs):
        self.get_object = self.get_instance
        return self.retrieve(request, *args, **kwargs)

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
