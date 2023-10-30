from drf_spectacular.utils import extend_schema
from rest_framework import views, status
from rest_framework.response import Response

from apps.attributes.selectors import get_atrributes

from .serializers import AttributesSerializer


@extend_schema(responses=AttributesSerializer)
class AttributesView(views.APIView):
    """Просмотр всех доступных атрибутов."""

    def get(self, request):
        data = get_atrributes()
        serializer = AttributesSerializer(instance=data)
        return Response(serializer.data, status=status.HTTP_200_OK)
