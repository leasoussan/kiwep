from django.urls import path

from .team_views import (
    TeamListAPIView,
    TeamDetailAPIView,
    TeamUpdateAPIView,
    TeamDeleteAPIView,
    TeamCreateAPIView,
)

urlpatterns = [
    path('team_list/', TeamListAPIView.as_view(), name='api_team_list'),
    path('team_detail/<int:pk>', TeamDetailAPIView.as_view(), name='api_team_detail'),
    path('team_update/<int:pk>', TeamUpdateAPIView.as_view(), name='api_team_update'),
    path('team_delete/<int:pk>', TeamDeleteAPIView.as_view(), name='api_team_delete'),
    path('team_create/', TeamCreateAPIView.as_view(), name='api_team_create')
]