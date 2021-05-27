from django.urls import path

from .project_views import (
    ProjectListAPIView,
    ProjectDetailAPIView,
    ProjectUpdateAPIView,
    ProjectDeleteAPIView,
    ProjectCreateAPIView,
)

urlpatterns = [
    path('project_list/', ProjectListAPIView.as_view(), name='api_project_list'),
    path('project_detail/<int:pk>', ProjectDetailAPIView.as_view(), name='api_project_detail'),
    path('project_update/<int:pk>', ProjectUpdateAPIView.as_view(), name='api_project_update'),
    path('project_delete/<int:pk>', ProjectDeleteAPIView.as_view(), name='api_project_delete'),
    path('project_create/', ProjectCreateAPIView.as_view(), name='api_project_create'),
]
