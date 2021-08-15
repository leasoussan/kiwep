from django.contrib import messages
from django.shortcuts import render, reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import user_passes_test, login_required
from django.urls import reverse_lazy
from accounts.forms import SpeakerInviteForm
from accounts.decorators import check_profile
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView

from content.models import Project, Team, Mission, Resource
from .models import Institution
from content.managers import ProjectModelManager, TeamModelManager, MissionModelManager, ResourceModelManager
from accounts.mixin import ProfileCheckPassesTestMixin, SpeakerStatuPassesTestMixin, RepresentativeStatuPassesTestMixin
from .forms import InstitutionAddForm
User = get_user_model()




@login_required
@user_passes_test(check_profile, login_url='create_profile')
def dashboard(request):
    context= {
        'form': SpeakerInviteForm()
    }
    return render(request, "backend/general_dashboard.html", context)

@login_required
@user_passes_test(check_profile, login_url= 'create_profile')
def my_calendar_view(request):
    return render(request, 'backend/my_calendar.html')





@login_required
@user_passes_test(check_profile, login_url= 'create_profile')
def team_board(request):

    return render(request, "backend/team_board.html" )


