from django.urls import path
from content.views_project import *
from content.views_team import *
from content.views_mission import *
from content.views_resource import *
from .views import *



urlpatterns = [

    path('', homepage_view, name = 'homepage'),
    # project

    path('chose-project-detail/<int:pk>', ChooseProjectView.as_view(), name = "chose_project_detail"),
    path('project-list/', ProjectListView.as_view(), name = "project_list"),
    path('student-available-project-list/', StudentAvailableTeamList.as_view(), name="student_available_project_list"),
    path('project-detail/<int:pk>', ProjectDetailView.as_view(), name = "project_detail"),
    path('create-project/', ProjectCreateView.as_view(), name ="create_project"),
    path('duplicate-project/<int:pk>/<int:team_id>/', DuplicateProjectCreateView.as_view(), name="duplicate_create_project"),

    path('create-project-mission/<int:pk>', CreateProjectMissionView.as_view(), name="create_project_mission"),
    path('update-project/<int:pk>', ProjectUpdateView.as_view(), name = "update_project"),
    path('delete-project/<int:pk>', ProjectDeleteView.as_view(), name = "delete_project"),




    # mission
    path('mission-list/', IndividualMissionListView.as_view(), name="mission_list"),
    path('my_mission-list/', IndividualMissionListView.as_view(), name="my_mission_list"),
    path('individual-mission-detail/<int:pk>', IndividualMissionDetailView.as_view(), name="individual_mission_detail"),
    path('collective-mission-detail/<int:pk>', CollectiveMissionDetailView.as_view(), name="collective_mission_detail"),
    path('assign-collective-mission-detail/<int:pk>', AssignCollectiveMissionView.as_view(), name="assign_collective_mission_detail"),

    path('create-individual-mission/<int:project_id>', AddIndividualMissionView.as_view(),
         name="create_individual_mission"),
    path('create-collective-mission/<int:project_id>', AddCollectiveMissionView.as_view(),
         name="create_collective_mission"),
    path('update-individual-mission/<int:pk>', IndividualMissionUpdateView.as_view(), name="update_individual_mission"),
    path('update-collective-mission/<int:pk>', CollectiveMissionUpdateView.as_view(), name="update_collective_mission"),
    path('delete-mission/<int:pk>', MissionDeleteView.as_view(), name="delete_mission"),
    path('claim-mission/<int:pk>', ClaimMission.as_view(), name="claim_mission"),
    path('submit-mission/<int:pk>', StudentSubmitMission.as_view(), name='submit_mission'),
    path('unclaim-mission/<int:pk>', UnclaimMission.as_view(), name="unclaim_mission"),




    # team
    path('team-list/', TeamListView.as_view(), name = "team_list"),
    path('team-detail/<int:pk>', TeamDetailView.as_view(), name = "team_detail"),
    path('create-team/', TeamCreateView.as_view(), name = "create_team"),
    path('chose-project-team/<int:pk>/<int:team_pk>', ChooseTeamProjectView.as_view(), name = "chose_team_project"),
    path('create-team-project/<int:pk>', ProjectTeamCreateView.as_view(), name = "create_team_project"),

    path('update-mission/<int:pk>', TeamEditIndividualProjectMission.as_view(), name = "update_individual_mission"),#update single mission

    path('update-team-mission/<int:pk>', TeamEditCollectiveProjectMission.as_view(), name = "update_team_mission"),#update single mission

    path('add-member-team/<int:pk>', AddTeamMemberView.as_view(), name = "add_member_team"),

    path('join-team/<int:pk>', JoinTeamView.as_view(), name = "join_team"),
    path('leave-team/<int:pk>', LeaveTeamView.as_view(), name = "leave_team"),

    path('update-team/<int:pk>', TeamUpdateView.as_view(), name = "update_team"),
    path('delete-team/<int:pk>', TeamDeleteView.as_view(), name = "delete_team"),






    # ressource
    path('resource-list/<int:pk>', ProjectResourceListView.as_view(), name = "resource_list"),
    path('resource-detail/<int:pk>', ResourceDetailView.as_view(), name = "resource_detail"),
    path('create-resource/', ResourceCreateView.as_view(), name = "create_resource"),
    path('update-resource/<int:pk>', ResourceUpdateView.as_view(), name = "update_resource"),
    path('delete-resource/<int:pk>', ResourceDeleteView.as_view(), name = "delete_resource"),


]
