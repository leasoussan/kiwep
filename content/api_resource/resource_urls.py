from django.urls import path

from .resource_views import (
    ResourceListAPIView,
    ResourceDetailAPIView,
    ResourceUpdateAPIView,
    ResourceDeleteAPIView,
    ResourceCreateAPIView,
)

urlpatterns = [
    path('resource_list/', ResourceListAPIView.as_view(), name='api_resource_list'),
    path('resource_detail/<int:pk>', ResourceDetailAPIView.as_view(), name='api_resource_detail'),
    path('resource_update/<int:pk>', ResourceUpdateAPIView.as_view(), name='api_resource_update'),
    path('resource_delete/<int:pk>', ResourceDeleteAPIView.as_view(), name='api_resource_delete'),
    path('resource_create/', ResourceCreateAPIView.as_view(), name='api_resource_create'),
]