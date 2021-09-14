from django.contrib import messages
from django.shortcuts import render, reverse, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import user_passes_test, login_required
from django.urls import reverse_lazy
from django.views import View

from accounts.forms import SpeakerInviteForm
from accounts.decorators import check_profile
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView

from accounts.models import Student
from .models import Institution, Group
from accounts.mixin import ProfileCheckPassesTestMixin, SpeakerStatuPassesTestMixin, RepresentativeStatuPassesTestMixin
from .forms import InstitutionAddForm, InstitutionAddGroupForm

User = get_user_model()




@login_required
@user_passes_test(check_profile, login_url='create_profile')
def dashboard(request):
    if request.user.is_representative:
        institution_groups = Group.objects.all()
        context = {
            'speaker_invite_form': SpeakerInviteForm(),
            'add_group_form': InstitutionAddGroupForm(),
            'institution_group': institution_groups,

        }

    else:

        teams = request.user.profile().team_set.all()
        participants = Student.objects.filter(team__in=teams).distinct()

        context= {
            'add_group_form': InstitutionAddGroupForm(),
            'participants':participants,
        }
    return render(request, "backend/general_dashboard.html", context)





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