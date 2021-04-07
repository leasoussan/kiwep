from django.shortcuts import render, reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import user_passes_test, login_required
from accounts.decorators import check_profile
from content.models import Project, Team, Mission, Resource
from content.managers import ProjectModelManager, TeamModelManager, MissionModelManager, ResourceModelManager
User = get_user_model()



@login_required
@user_passes_test(check_profile, login_url= 'create_profile')
def dashboard(request):
    print(request.COOKIES)
    return render(request, "backend/general_dashboard.html" )

@login_required
@user_passes_test(check_profile, login_url= 'create_profile')
def my_calendar_view(request):
    return render(request, 'backend/my_calendar.html')





@login_required
@user_passes_test(check_profile, login_url= 'create_profile')
def team_board(request):

    return render(request, "backend/team_board.html" )


