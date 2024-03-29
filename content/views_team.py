from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from .models import Team, CollectiveMission, Project, Mission, IndividualMission, IndividualCollectiveMission
from django.forms import ModelForm
from .forms import TeamAddForm, AddMemberTeamForm, ProjectAddForm, UpdateTeamForm, ProjectTeamAddForm, \
    IndividualMissionAddForm, CollectiveMissionAddForm, BulkAddMissionForm

from django.urls import reverse_lazy
from django.views.generic.base import RedirectView

from django.contrib import messages


from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
    View,
)

from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.mixin import ProfileCheckPassesTestMixin, SpeakerStatuPassesTestMixin



class TeamListView(ProfileCheckPassesTestMixin, ListView):
    """ Team List View will Show a user Teams list"""
    model = Team
    template_name = 'backend/team/team_list.html'
    context_object_name = 'team_list'


    def get_queryset(self):
        # return self.request.user.profile().team_set.filter(project__isnull=False, project__completed=False)

        # to get her all- we want only the active ones
        return self.request.user.profile().team_set.all()


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.is_speaker:
            context['project_form'] = ProjectAddForm()
            context['mission_bulk_form'] = BulkAddMissionForm(projects=self.request.user.profile().project_set.all())
            context['individual_form'] = IndividualMissionAddForm()
            context['collective_form'] = CollectiveMissionAddForm()
            context['project_form'] = ProjectAddForm()
            context['templates'] = Project.objects.personal_templates()
            context['old_projects'] = self.request.user.profile().project_set.all()
        return context

    def get_object(self):
        pk = self.kwargs.get("pk")
        return get_object_or_404(Team, pk=pk)



class TeamDetailView(ProfileCheckPassesTestMixin, DetailView):
    """ Global Team Details """

    model = Team
    template_name = 'backend/team/team_detail.html'
    # queryset = IndividualMission.objects.all().available_mission()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if not self.object.project and self.request.user.is_speaker:
            context['project_form'] = ProjectAddForm()
            context['templates'] = self.request.user.profile().project_set.personal_templates()
            context['old_projects'] = self.request.user.profile().project_set.filter(is_template=False)
        elif self.object.project and self.request.user.is_speaker:
            context['individual_form'] = IndividualMissionAddForm()
            context['collective_form'] = CollectiveMissionAddForm()
        elif self.request.user.is_student:
            context['mission_no_chapter'] = Mission.objects.filter(order=None)
            # to get her all individualcollective Mission
            #     context['individual_collective_mission']= IndividualCollectiveMission.objects.filter(parent_mission__project__id=self.object.project.id, attributed_to=self.request.user.profile())
        return context

    def get_object(self):
        pk = self.kwargs.get("pk")
        return get_object_or_404(Team, pk=pk)







class TeamCreateView(SpeakerStatuPassesTestMixin,  CreateView):
    """Create a Team View """
    model = Team
    form_class = TeamAddForm
    template_name = 'crud/create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'].fields['group_institution'].queryset = self.request.user.profile().group.all()
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.manager = self.request.user.profile()
        self.object.completed = False
        self.object.save()
        return super().form_valid(form)


    def get_success_url(self):
        return reverse_lazy('team_detail', kwargs={'pk':self.object.id})

    # def time_message(self, request):
    #     if Team.start_date > Team.due_date:
    #         messages.warning(request, 'Start date must be less than end date')
    #         return render(request, "create_team_mission.html")





class ProjectToTeamCreateView(TeamCreateView):
    """Create a Team for an existing project  """

    def form_valid(self, form):
        super().form_valid(form)
        print(form)
        pk = self.kwargs.get('pk')
        print('pk', pk)
        self.object.project = Project.objects.get(pk=pk)
        self.object.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('team_detail', kwargs={'pk': self.object.id})


#
# class TeamCreateMissionView(SpeakerStatuPassesTestMixin, View):
#     """ Once a Team IS created the missions have to be set, Deadline, attribution etc...."""
#     def get(self, request, *args, **kwargs):
#
#         team = Team.objects.get(id = self.kwargs['pk'])
#         participants= team.participants.all()
#
#
#
#         return render(request, 'crud/create_team_missions.html', {'participants': participants})
#
#
#     def post(self, request, *args, **kwargs):
#
#         team = Team.objects.get(id = self.kwargs['pk'])
#         missions = team.project.missions.all()
#
#         formset = CollectiveMissionFormSet(request.POST, instance = team)
#
#
#         if formset.is_valid():
#             formset.save()
#             return redirect('team_detail' , team.id)
#
#
#         for form in formset:
#             form.fields['mission'].queryset = missions
#
#         return render(request, 'crud/create_team_missions.html', {'formset': formset})
#


# prefix='collective' We might need to add a Prefix if using few formset- might have been changed by DJANGO 

#
# class TeamEditIndividualProjectMission(SpeakerStatuPassesTestMixin, UpdateView):
#     """ """
#     model = IndividualMission
#     fields = '__all__'
#
#     template_name = 'crud/update.html'
#     # success_url = ('team_detail')
#
#
#
# class TeamEditCollectiveProjectMission(SpeakerStatuPassesTestMixin, UpdateView):
#     model = CollectiveMission
#     fields = '__all__'
#
#     template_name = 'crud/update.html'
#     # success_url = ('team_detail')




class TeamUpdateView(LoginRequiredMixin, SpeakerStatuPassesTestMixin, UpdateView):
    model = Team
    form_class = UpdateTeamForm
    template_name = 'crud/update.html'
    # success_url = ('team_detail')


    def form_valid(self,form):
        return super().form_valid(form)

    def get_object(self):
        pk = self.kwargs.get("pk")
        return get_object_or_404(Team, pk=pk)


class TeamDeleteView(LoginRequiredMixin, SpeakerStatuPassesTestMixin, DeleteView):
    model = Team
    template_name = 'crud/delete.html'
    success_url = reverse_lazy('team_list')

    def get_object(self):
        pk = self.kwargs.get("pk")
        return get_object_or_404(Team, pk=pk)












class JoinTeamView(LoginRequiredMixin, RedirectView):
    pattern_name = 'team_detail'


    def get_redirect_url(self, *args, **kwargs):
        team = get_object_or_404(Team, pk=kwargs['pk'])
        team.participants.add(self.request.user.profile())

        return super().get_redirect_url(*args, **kwargs)


class LeaveTeamView(LoginRequiredMixin, RedirectView):
    pattern_name= 'team_list'

    def get_redirect_url(self, *args, **kwargs):
        team = get_object_or_404(Team, pk=kwargs['pk'])
        team.participants.remove(self.request.user.profile())
        del kwargs['pk']
        return super().get_redirect_url(*args, **kwargs)



class AddTeamMemberView(LoginRequiredMixin, UpdateView):
    model = Team
    template_name = 'crud/update.html'
    success_url = ('team_detail')
    form_class = AddMemberTeamForm

    def get_success_url(self):
        return reverse_lazy('team_detail', kwargs={'pk': self.object.id})

    def form_invalid(self, form):
        print("error")
        print(form.errors)
        return super().form_invalid(form)