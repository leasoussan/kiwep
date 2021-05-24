
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
    CreateAPIView,
    RetrieveUpdateAPIView,
)

from rest_framework.response import Response
from rest_framework.decorators import api_view

from content.models import Resource
from .resource_serializer import (
    ResourceListSerializer,
    ResourceDetailSerializer,
    ResourceCreateUpdateSerializer,
)


@api_view(['GET'])
def resourceOverview(request):
    resource_urls = {
        'List': '/resource_list/',
        'Detail View': '/resource_detail/<str:pk>/',
        'Create': '/resource_create/',
        'Update': '/resource_update/<str:pk>/',
        'Delete': '/resource_delete/<str:pk>/',
    }
    return Response(resource_urls)


class ResourceCreateAPIView(CreateAPIView):
    queryset = Resource.objects.all()
    serializer_class = ResourceCreateUpdateSerializer

    def perform_create(self, serializer):
        serializer.save()


class ResourceDetailAPIView(RetrieveAPIView):
    queryset = Resource.objects.all()
    serializer_class = ResourceDetailSerializer

    # if we want to change the lookup in url
    # lookup_url_kwarg = "What I want to "/


class ResourceUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Resource.objects.all()
    serializer_class = ResourceCreateUpdateSerializer

    def perform_update(self, serializer):
        serializer.save()


class ResourceDeleteAPIView(DestroyAPIView):
    queryset = Resource.objects.all()
    serializer_class = ResourceDetailSerializer


class ResourceListAPIView(ListAPIView):
    queryset = Resource.objects.all()
    serializer_class = ResourceListSerializer
