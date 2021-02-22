from django.urls import path
from content.views_project import * 
from content.views_team import * 

urlpatterns = [
    path('project-list/', ProjectListView.as_view(), name = "project_list"),
    path('project-detail/<int:pk>', ProjectDetailView.as_view(), name = "project_detail"),
    path('create-project/', ProjectCreatelView.as_view(), name = "create_project"),
    path('update-project/<int:pk>', ProjectUpdateView.as_view(), name = "update_project"),
    path('delete-project/<int:pk>', ProjectDeleteView.as_view(), name = "delete_project"),


    # team 
    path('team-list/', TeamListView.as_view(), name = "team_list"),
    path('team-detail/<int:pk>', TeamDetailView.as_view(), name = "team_detail"),
    path('create-team/', TeamCreatelView.as_view(), name = "create_team"),
    path('update-team/<int:pk>', TeamUpdateView.as_view(), name = "update_team"),
    path('delete-team/<int:pk>', TeamDeleteView.as_view(), name = "delete_team"),
]
