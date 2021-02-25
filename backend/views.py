from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import user_passes_test, login_required
from content.models import Project, Team, Mission, Resource
# Create your views here.
User = get_user_model()

@login_required

def dashboard(request):
    projects = Project.objects.filter(speaker = request.user.id)[:5]
    teams = Team.objects.filter(project__speaker= request.user.id)[:5]
    missions = Mission.objects.filter(speaker = request.user.id)[:5]
    resources = Resource.objects.filter(speaker = request.user.id)[:5]
    context = {
        'projects': projects,
        'teams':teams,
        'resources':resources,
        'mission': missions,
    }

    return render(request, "backend/general_dashboard.html", context)

  
