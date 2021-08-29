from optparse import Option

from django.utils import timezone

from django.shortcuts import render, redirect, get_object_or_404
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






# class ChooseTeamProjectView(SpeakerStatuPassesTestMixin, RedirectView):
#     """Select a project will make you own a version of the project
#     This View will make himself a speaker to the project -
#     as a copy to enable using it after with a team and make changes"""
#
#     # query_sting = False >>this is false by default
#     pattern_name = 'team_detail'
#
#     def get_redirect_url(self,  *args, **kwargs):
#         project = get_object_or_404(Project, pk=kwargs['pk'])
#         team = get_object_or_404(Team, pk=kwargs['team_pk'])
#         project.id = None
#         project.is_template = False
#         project.is_global= False
#         project.is_premium= False
#         project.speaker = self.request.user.profile()
#         project.save()
#         team.project = project
#         team.save()
#         kwargs['pk'] = team.pk
#         del kwargs['team_pk']
#         return super().get_redirect_url(*args, **kwargs)
#





class ProjectListView(SpeakerStatuPassesTestMixin, ListView):
    model = Project
    template_name = 'backend/project/project_list.html'
    context_object_name = 'project_list'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data( *args, **kwargs)
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
    template_name = 'backend/project/team_list.html'
    context_object_name = "available_projects"


    def get_queryset(self):
        if self.request.user.is_student:
            return self.request.user.profile().class_level.team_set.filter(project__isnull=True)



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
        return reverse_lazy('project_detail', kwargs ={'pk':self.object.id} )




class ProjectTeamCreateView(ProjectCreateView):
    """This View inherite form ProjectCreateView project created with a team already exisiting
     we add here the team that it connecte right away with it and save it with a team """

    def form_valid(self, form):
        super().form_valid(form)
        pk = self.kwargs.get("pk")
        team= get_object_or_404(Team, pk=pk)
        team.project = self.object
        team.save()
        return super().form_valid(form)

# To Overwrite the Get_absolut_url if I want it to go somewhere else - for ex in the update view 

# def get_success_url(self):
#     return ('content/project_list')


def clean_missions(request, project_id, *querysets):
    for qs in querysets:
        objects = []
        if qs.model not in [IndividualMission, CollectiveMission]:
            print('Function clean mission should be only used on mission query set ')
            return
        for mission in qs:
            mission.id = None
            mission.owner = request.user
            mission.project_id = project_id
            mission.created_date = None
            mission.due_date = timezone.now()
            mission.completed = False
            print(dir(mission))
            if qs.model == IndividualMission:
                mission.attributed_to = None
                mission.accepted = False
            print('mission_cleaning line 190', mission)
            objects.append(mission)
        qs.model.objects.bulk_create(objects)




def clean_p_resource(project_id, queryset):

    objects = []
    if queryset.model is not Resource:
        print('Function clean resource should be only used on resource query set ')
        return
    for resource in queryset:
        resource.id = None
        resource.project_id = project_id
        objects.append(resource)
    queryset.model.objects.bulk_create(objects)


def clean_m_resource(mission_id, queryset):
    objects = []
    if queryset.model is not Resource:
        print('Function clean resource should be only used on resource query set ')
        return
    for resource in queryset:
        resource.id = None
        resource.mission_id = mission_id
        objects.append(resource)
    queryset.model.objects.bulk_create(objects)


# TODO: Add other clean
# def clean_skills(project_id, queryset):
#     objects = []
#     if queryset.model is not Skills:
#         print('Function clean skills should be only used on skills query set ')
#         return
#     for skill in queryset:
#         objects.append(skill)
#     queryset.model.objects.bulk_create(objects)






def get_due_date(self, **kwargs):
    context = super(ProjectTeamCreateView, self).get_due_date(**kwargs)
    context['options_list'] = Option.objects.all()
    return context



class ChooseProjectView(SpeakerStatuPassesTestMixin, RedirectView):
    """Select a template project will make you own a version of the project
    This View will make himself a speaker to the project -
    as a copy to enable using it after with a team and make changes -From Team Page"""

    # query_sting = False >>this is false by default
    pattern_name = 'update_project'

    def get_redirect_url(self, *args, **kwargs):
        project = get_object_or_404(Project, pk=kwargs['pk'])
        pk = self.kwargs.get("team_id")
        team = get_object_or_404(Team, pk=pk)
        missions = project.mission_set.filter(mission_type='i')
        print('mission_line 257', missions)
        project.id = None
        team.project = project
        project.is_template = False
        project.is_global = False
        project.is_premium = False
        project.speaker = self.request.user.profile()
        p_resources = project.resource_set.all()

        clean_missions(project.id, missions)
        clean_p_resource(project.id, p_resources)
        project.save()
        team.save()
        print('team_save')
        # del kwargs['pk']
        kwargs['pk'] = project.pk
        del kwargs['team_id']
        return super().get_redirect_url(*args, **kwargs)

    # def get_redirect_url(self,  *args, **kwargs):
    #     project = get_object_or_404(Project, pk=kwargs['pk'])
    #     pk = self.kwargs.get("team_id")
    #     team = get_object_or_404(Team, pk=pk)
    #     # print(team, 'team')
    #     missions = project.mission_set.all()
    #     individual_mission = missions.filter(individualmission=True)
    #     print('mission', missions)
    #     p_resources = project.resource_set.all()
    #
    #     project.id=None
    #     project.is_template=False
    #     project.is_global=False
    #     project.is_premium=False
    #     project.speaker = self.request.user.profile()
    #     project.save()
    #     clean_missions(project.id, individual_mission)
    #     clean_p_resource(project.id, p_resources)
    #     team.project = project
    #     del kwargs['team_id']
    #     kwargs['pk'] = project.pk
    #     return super().get_redirect_url(*args, **kwargs)








class DuplicateProjectCreateView(SpeakerStatuPassesTestMixin, RedirectView):
    """"""

    pattern_name = 'update_project'

    def get_redirect_url(self, *args, **kwargs):
        project = get_object_or_404(Project, pk=kwargs['pk'])
        pk = self.kwargs.get("team_id")
        team = get_object_or_404(Team, pk=pk)
        missions = project.mission_set.all()
        resources = project.resource_set.all()
        project.id =None
        project.save()
        clean_missions(project.id, missions)
        clean_p_resource(project.id, resources)
        team.project = project
        # {TODO:why team.project }
        team.save()
        kwargs['pk'] = project.pk
        del kwargs['team_id']
        return super().get_redirect_url(*args, **kwargs)




#
#
# class CreateProjectMissionView(SpeakerStatuPassesTestMixin, View):
#     """ Once a Project IS created the missions have to be set, Deadline, attribution etc...."""
#
#     def get(self, request, *args, **kwargs):
#
#         project = Project.objects.get(id=self.kwargs['pk'])
#
#         formset_collective = CollectiveMissionFormSet(instance=project)
#         formset_individual = IndividualMissionFormSet(instance=project)
#         formsets = {'individual':formset_individual, 'collective': formset_collective}
#
#
#         return render(request, 'crud/create_missions.html', {'formsets': formsets})
#
#     def post(self, request, *args, **kwargs):
#
#         project = Project.objects.get(id=self.kwargs['pk'])
#
#         individual_missions = IndividualMissionFormSet(request.POST, instance=project)
#
#         collective_missions = CollectiveMissionFormSet(request.POST, instance=project)
#
#         if individual_missions.is_valid():
#             individual_missions.save()
#             return redirect('project_detail', project.id)
#
#         return render(request, 'crud/create_project_missions.html', {'formset': individual_missions})
#
#







# -----------------------------PROJECT-----UpdateView:


class ProjectUpdateView(LoginRequiredMixin, SpeakerStatuPassesTestMixin, UpdateView):
    model = Project
    fields = [
        'name',
        'description',
        'time_to_complete',
        'points',
        'acquired_skills',
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

# 
# -----------------------------PROJECT-----:Delete View 

class ProjectDeleteView(LoginRequiredMixin, SpeakerStatuPassesTestMixin, DeleteView):
    model = Project
    template_name = 'crud/delete.html'
    success_url = reverse_lazy('project_list')

    def get_object(self):
        pk = self.kwargs.get("pk")
        return get_object_or_404(Project, pk=pk)


# author = Project.objects.get(name=)
# formset = BookFormSet(instance=author)




