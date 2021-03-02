from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import user_passes_test, login_required
from accounts.decorators import check_profile
from content.models import Project, Team, Mission, Resource
from content.managers import ProjectModelManager, TeamModelManager, MissionModelManager, ResourceModelManager
User = get_user_model()



@login_required
@user_passes_test(check_profile, login_url= 'create_profile/')
def dashboard(request):
    # projects = Project.objects.get_speaker_projects(request.user)
    # teams = Team.objects.get_speaker_teams(request.user)
    # missions = Mission.objects.get_speaker_missions(request.user)
    # resources = Resource.objects.get_speaker_resources(request.user)
    # context = {
    #     'projects': projects,
    #     'teams':teams,
    #     'resources':resources,
    #     'missions': missions,
    # }
    
    return render(request, "backend/general_dashboard.html" )



# def speaker_dashboard_content():
#     projects = Project.objects.get_speaker_projects(user)
#     teams = Team.objects.get_speaker_teams(user)
#     missions = Mission.objects.get_speaker_missions(user)
#     resources = Resource.objects.get_speaker_resources(user)
#     context = {
#         'projects': projects,
#         'teams':teams,
#         'resources':resources,
#         'missions': missions,
#     }
#     return context

