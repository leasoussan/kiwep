from django.urls import path
from .views import (
    dashboard,
    InstitutionAddGroupView, ProjectMissionBoardView,

)



urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),

    path('add_group/', InstitutionAddGroupView.as_view(), name='add_group'),
    path('mission_board/<int:pk>/', ProjectMissionBoardView.as_view(), name='project_mission_board')

]
