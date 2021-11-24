import json
from datetime import datetime

from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import user_passes_test, login_required
from django.urls import reverse_lazy
from django.views import View
from django.views.decorators.http import require_POST
from django.views.generic import RedirectView

from accounts.forms import SpeakerInviteForm
from accounts.decorators import check_profile, speaker_check
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView

from accounts.models import Student
from content.models import Project, Mission, Chapter
from .models import Institution, Group
from accounts.mixin import ProfileCheckPassesTestMixin, SpeakerStatuPassesTestMixin, RepresentativeStatuPassesTestMixin
from .forms import InstitutionAddForm, InstitutionAddGroupForm

User = get_user_model()




@login_required
@user_passes_test(check_profile, login_url='create_profile')
def dashboard(request):
    if request.user.is_representative:

        institution_groups = request.user.profile().institution.group_set.all()
        context = {
            'speaker_invite_form': SpeakerInviteForm(),
            'add_group_form': InstitutionAddGroupForm(),
            'institution_group': institution_groups,
        }
        return render(request, "backend/general_dashboard.html", context)

    elif request.user.is_speaker:
        teams = request.user.profile().team_set.all()
        participants = Student.objects.filter(team__in=teams).distinct()
        context= {
            'add_group_form': InstitutionAddGroupForm(),
            'participants': participants,
        }
        return render(request, "backend/general_dashboard.html", context)

    else:
        context = {

        }

        return render(request, "backend/general_dashboard.html", context)

# TODO avi ?? The USage
# def get_current_date_time(request):
#     date_time_now = datetime.datetime.now()
#     date_time_dict = {
#         'date_time_key': date_time_now,
#     }
#     return render(request, 'backend/general_dashboard.html', date_time_dict)

class InstitutionAddGroupView(ProfileCheckPassesTestMixin, View):


    def post(self, request):
        if request.method == "POST":
            form = InstitutionAddGroupForm(request.POST)
            institution = request.user.profile().institution
            if form.is_valid():
                add_group = form.save(commit=False)
                add_group.institution = institution
                add_group.save()

            return redirect('dashboard')

        return redirect('dashboard')


class ProjectMissionBoardView(DetailView):
    model = Project
    template_name = 'backend/project/project_board/project_mission_board.html'


class CreateChapterRedirectView(RedirectView):
    pattern_name = 'project_detail'

    def get_redirect_url(self, *args, **kwargs):
        proj = get_object_or_404(Project, id=kwargs['pk'])
        if proj.speaker == self.request.user.profile():
            proj.chapter_set.create(name=f'Chapter {proj.next_chapter_num()}')
        return super().get_redirect_url(*args, **kwargs)

# @login_required
# @user_passes_test(speaker_check, login_url='create_profile')
@require_POST
def change_mission_chapter(request):
    data = json.loads(request.body)
    chapter_id = data.get('chapter_id')
    previous_id = data.get('previous_id')
    mission = get_object_or_404(Mission, id=data.get('mission_id'))
    mission.chapter = None if chapter_id == 0 else get_object_or_404(Chapter, id=chapter_id)

    if previous_id:
        prev_mission = get_object_or_404(Mission, id=previous_id)
        mission.order = prev_mission.order + 1
        # mission.save()
        # print("view_114mission_with_prev_saved", mission.order)
    elif mission.chapter:
        mission.order = 1
    mission.save()

    return HttpResponse('ok')