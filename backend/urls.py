from django.urls import path
from .views import (
    dashboard,
    InstitutionAddGroupView, ProjectMissionBoardView, CreateChapterRedirectView, change_mission_chapter

)



urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),

    path('add_group/', InstitutionAddGroupView.as_view(), name='add_group'),
    path('mission_board/<int:pk>/', ProjectMissionBoardView.as_view(), name='project_mission_board'),
    path('chapter/<int:pk>/create', CreateChapterRedirectView.as_view(), name='create_chapter'),
    path('change_mission_chapter/', change_mission_chapter, name='change_mission_chapter')

]
