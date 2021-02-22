from django.urls import path
from django.contrib import admin 

from .views import (
    ProjectListAPIView,
    ProjectDetailAPIView,
    ProjectUpdateAPIView,
    ProjectDeleteAPIView,
    ProjectCreateAPIView,
)


urlpatterns=[
    path('project/' ,ProjectListAPIView.as_view(), name='api_project_list'),
    path('project/<int:pk>' ,ProjectDetailAPIView.as_view(), name='api_project_detail'),
    path('project/<int:pk>' ,ProjectUpdateAPIView.as_view(), name='api_project_update'),
    path('project/<int:pk>' ,ProjectDeleteAPIView.as_view(), name='api_project_delete'),
    path('project/' ,ProjectCreateAPIView.as_view(), name='api_project_create'),
]

 