from optparse import Option

from django.utils import timezone

from django.shortcuts import render, redirect, get_object_or_404

from .clone_helpers import clone_project
from .models import Project, Team, IndividualMission, CollectiveMission, Resource, Mission, Skills
from django.forms import ModelForm
from .forms import (
    ProjectAddForm,
    # IndividualMissionFormSet,
    # CollectiveMissionFormSet,
    IndividualMissionAddForm,
    CollectiveMissionAddForm, ResourceAddForm, BulkAddMissionForm,
)
from django.urls import reverse_lazy

from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
    View, RedirectView,
)

from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.mixin import ProfileCheckPassesTestMixin, SpeakerStatuPassesTestMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin




class ProjectListView(SpeakerStatuPassesTestMixin, ListView):
    model = Project
    template_name = 'backend/project/project_list.html'
    context_object_name = 'project_list'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['project_form'] = ProjectAddForm()
        context['mission_bulk_form'] = BulkAddMissionForm(projects=self.request.user.profile().project_set.personal_projects())
        context['individual_form'] = IndividualMissionAddForm()
        context['collective_form'] = CollectiveMissionAddForm()
        context['templates'] = Project.objects.personal_templates().filter(speaker=self.request.user.profile())
        context['old_projects'] = self.request.user.profile().project_set.all()
        return context

    def get_queryset(self):
        queryset = self.request.user.profile().project_set.personal_templates()
        queryset2 = super().get_queryset().global_template_projects()
        return queryset.union(queryset2)





class StudentAvailableTeamList(ProfileCheckPassesTestMixin, ListView):
    model = Team
    template_name = 'backend/project/team_list_student.html'
    # context_object_name = "available_projects"

    #
    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(*args, **kwargs)
    #     student = self.request.user.profile()
    #     context['available_projects'] = student.class_level.team_set.all()
    #     return context

    def get_queryset(self):
        if self.request.user.is_student:
            return self.request.user.profile().group_institution_set.team_set.all()


# ----------------PROJECT------Detail_View/

class ProjectDetailView(ProfileCheckPassesTestMixin, DetailView):
    model = Project
    template_name = 'backend/project/project_detail.html'


    def get_object(self):
        pk = self.kwargs.get("pk")
        return get_object_or_404(Project, pk=pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['individual_form'] = IndividualMissionAddForm()
        context['collective_form'] = CollectiveMissionAddForm()
        context['resources_form'] = ResourceAddForm()
        return context



# -----------------------------PROJECT-----Create_View:


class ProjectCreateView(SuccessMessageMixin, SpeakerStatuPassesTestMixin, CreateView):
    model = Project
    form_class = ProjectAddForm
    template_name = 'crud/create.html'
    success_message = "Your project was created successfuly"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.speaker = self.request.user.profile()
        self.object.completed = False
        self.object.save()

        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'You have an error in your form')
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('project_detail', kwargs={'pk': self.object.id} )




class ProjectTeamCreateView(ProjectCreateView):
    """This View inherite form ProjectCreateView project created with a team already exisiting
     we add here the team that it connecte right away with it and save it with a team """

    def form_valid(self, form):
        super().form_valid(form)
        pk = self.kwargs.get("pk")
        team = get_object_or_404(Team, pk=pk)
        team.project = self.object
        team.project.is_template = False
        team.save()
        return super().form_valid(form)


def get_due_date(self, **kwargs):
    context = super(ProjectTeamCreateView, self).get_due_date(**kwargs)
    context['options_list'] = Option.objects.all()
    return context


class ChooseProjectForTeamView(SpeakerStatuPassesTestMixin, RedirectView):
    """Select a project will make you own a version of the project
    This View will make himself a speaker to the project -
    as a copy to enable using it after with a team and make changes"""

    # query_sting = False >>this is false by default
    pattern_name = 'update_project'

    def get_redirect_url(self,  *args, **kwargs):
        project = get_object_or_404(Project, pk=kwargs['pk'])
        pk = kwargs['team_id']
        team = get_object_or_404(Team, pk=pk)
        new_proj = clone_project(project, self.request.user.profile())
        team.project = new_proj
        team.save()
        del kwargs['team_id']
        kwargs['pk'] = new_proj.pk
        return super().get_redirect_url(*args, **kwargs)


# -----------------------------PROJECT-----UpdateView:


class ProjectUpdateView(LoginRequiredMixin, SpeakerStatuPassesTestMixin, UpdateView):
    model = Project
    fields = [
        'name',
        'description',
        'time_to_complete',
        'points',
    ]
    template_name = 'crud/update.html'

    def get_object(self):
        pk = self.kwargs.get("pk")
        return get_object_or_404(Project, pk=pk)

    def form_valid(self,form):
        return super().form_valid(form)

    def get_due_date(self, **kwargs):
        context = super(ProjectUpdateView, self).get_due_date(**kwargs)
        context['options_list'] = Option.objects.all()
        return context


# -----------------------------PROJECT-----:Delete View 


class ProjectDeleteView(LoginRequiredMixin, SpeakerStatuPassesTestMixin, DeleteView):
    model = Project
    template_name = 'crud/delete.html'
    success_url = reverse_lazy('project_list')

    def get_object(self):
        pk = self.kwargs.get("pk")
        return get_object_or_404(Project, pk=pk)


