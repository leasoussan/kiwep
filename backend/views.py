from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import user_passes_test, login_required

from content.models import Project, Team, Mission, Resource
from content.managers import ProjectModelManager, TeamModelManager, MissionModelManager, ResourceModelManager
User = get_user_model()



@login_required
def dashboard(request, user):
    if user.get_user_type() == "student":
        context = student_dashboard_content(user)
    
    elif user.get_user_type() == "speaker":
        context = student_dashboard_content(user)


    
    return render(request, "backend/general_dashboard.html", context)





def student_dashboard_content(request):
    teams = Team.objects.filter(participants = request.user.id).all()
    projects = teams.project.all()
    missions =projects.mission.all()
    resources = missions.resources.all()
    context = {
        'projects': projects,
        'teams':teams,
        'resources':resources,
        'mission': missions,
    }
    return context


def speaker_dashboard_content(user):
    projects = Project.objects.get_speaker_projects(user)
    teams = Team.objects.get_speaker_teams(user)
    missions = Mission.objects.get_speaker_missions(user)
    resources = Resource.objects.get_speaker_resources(user)
    context = {
        'projects': projects,
        'teams':teams,
        'resources':resources,
        'missions': missions,
    }
    return context

