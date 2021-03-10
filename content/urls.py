from django.urls import path
from content.views_project import * 
from content.views_team import * 
from content.views_mission import *
from content.views_resource import *
from .views import * 


urlpatterns = [

    path('', homepage_view, name = 'homepage'),
    # project
    path('project-list/', ProjectListView.as_view(), name = "project_list"),
    path('project-detail/<int:pk>', ProjectDetailView.as_view(), name = "project_detail"),
    path('create-project/', ProjectCreatelView.as_view(), name = "create_project"),
    path('update-project/<int:pk>', ProjectUpdateView.as_view(), name = "update_project"),
    path('delete-project/<int:pk>', ProjectDeleteView.as_view(), name = "delete_project"),


    # team 
    path('team-list/', TeamListView.as_view(), name = "team_list"),
    path('team-detail/<int:pk>', TeamDetailView.as_view(), name = "team_detail"),
    path('create-team/', TeamCreateView.as_view(), name = "create_team"),
    path('create-team-missions/<int:id>', TeamCreateMissionView.as_view(), name = "create_team_missions"),
    
    path('update-team/<int:pk>', TeamUpdateView.as_view(), name = "update_team"),
    path('delete-team/<int:pk>', TeamDeleteView.as_view(), name = "delete_team"),


    # mission
    path('mission-list/', MissionListView.as_view(), name = "mission_list"),
    path('mission-detail/<int:pk>', MissionDetailView.as_view(), name = "mission_detail"),
    path('create-mission/', MissionCreateView.as_view(), name = "create_mission"),
    path('update-mission/<int:pk>', MissionUpdateView.as_view(), name = "update_mission"),
    path('delete-mission/<int:pk>', MissionDeleteView.as_view(), name = "delete_mission"),


    # ressource 
    path('resource-list/', ResourceListView.as_view(), name = "resource_list"),
    path('resource-detail/<int:pk>', ResourceDetailView.as_view(), name = "resource_detail"),
    path('create-resource/', ResourceCreateView.as_view(), name = "create_resource"),
    path('update-resource/<int:pk>', ResourceUpdateView.as_view(), name = "update_resource"),
    path('delete-resource/<int:pk>', ResourceDeleteView.as_view(), name = "delete_resource"),


    # development link - to view
    path('content-manager/', content_manager, name="content_manager"),
]


