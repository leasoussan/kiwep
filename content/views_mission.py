from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from message.forms import AddAnswerForm, MissionSpeakerStatusAnswerForm
from .models import Mission, CollectiveMission, Team, IndividualMission, IndividualCollectiveMission, Project
from django.forms import ModelForm
from .forms import (
    IndividualMissionAddForm,
    CollectiveMissionAddForm,
    CollectiveMissionAssign,
    ValidateMissionForm,
    ResourceAddForm, BulkAddMissionForm,

)
from django.urls import reverse_lazy
from django.views.generic.base import RedirectView

from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
    View, FormView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.mixin import ProfileCheckPassesTestMixin, SpeakerStatuPassesTestMixin, StudentStatuPassesTestMixin




# ----------------------------------------------------------------------------------------------------------------

class IndividualMissionListView(ProfileCheckPassesTestMixin, ListView):
    ''' To See all Missions View'''
    model = IndividualMission
    template_name = 'backend/mission/my_mission_list.html'
    context_object_name = 'mission_list'


    def get_queryset(self):
        return super().get_queryset().filter(attributed_to=self.request.user.profile())


# ----------------------------------------------------------------------------------------------------------------

class AnswerBoardMissionListView(ProfileCheckPassesTestMixin, ListView):
    ''' To See all Missions View'''
    model = IndividualMission
    template_name = 'backend/mission/my_mission_list.html'
    context_object_name = 'answers_mission_list'
    form = ValidateMissionForm()


    def get_queryset(self):
        return super().get_queryset().filter(attributed_to__isnull=False)

# ----------------------------------------------------------------------------------------------------------------



class AddIndividualMissionView(SpeakerStatuPassesTestMixin, View):

    ''' Add an Individual Mission '''
    model = IndividualMission

    def get(self, request, *args, **kwargs):
        mission_form = IndividualMissionAddForm(instance=request.user)
        return redirect('homepage')

    def post(self, request, *args, **kwargs):
        mission_form = IndividualMissionAddForm(request.POST)


        if mission_form.is_valid():
            mission = mission_form.save(commit=False)
            mission.project_id=kwargs['project_id']
            mission.mission_type = 'i'
            mission.owner = self.request.user
            mission.save()

            return redirect('individual_mission_detail', mission.id)

        return render(request, 'backend/mission/mission_detail.html',
                      {'mission_form': mission_form})


# ----------------------------------------------------------------------------------------------------------------






class AddCollectiveMissionView(SpeakerStatuPassesTestMixin, View):
    ''' Add an Individual Mission '''
    model = CollectiveMission

    def get(self, request, *args, **kwargs):
        mission_form = CollectiveMissionAddForm(instance=request.user)
        return redirect('homepage')

    def post(self, request, *args, **kwargs):
        mission_form = CollectiveMissionAddForm(request.POST)

        if mission_form.is_valid():
            mission = mission_form.save(commit=False)
            mission.project_id = kwargs['project_id']
            mission.mission_type = 'c'
            mission.owner = self.request.user
            mission.save()

            return redirect('collective_mission_detail', mission.id)

        return render(request, 'backend/mission/mission_detail.html',
                      {'mission_form': mission_form})


# -------------------------------------------------------------------------------------------------------------------------







# ----------------------------------------------------------------------------------------------------------------

class IndividualMissionDetailView(ProfileCheckPassesTestMixin, DetailView):
    '''Detail Of General Mission'''
    model = IndividualMission
    template_name = 'backend/mission/mission_detail.html'    
    
    

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(IndividualMission, pk=pk)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['resources_form'] = ResourceAddForm()
        context['answer_form'] = AddAnswerForm()
        context['status_form'] = MissionSpeakerStatusAnswerForm()
        return context
# ----------------------------------------------------------------------------------------------------------------





class CollectiveMissionDetailView(ProfileCheckPassesTestMixin, DetailView):
    '''Detail Of General Mission'''
    model = CollectiveMission
    template_name = 'backend/mission/mission_detail.html'

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(CollectiveMission, pk=pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['resources_form'] = ResourceAddForm()
        context['answer_form'] = AddAnswerForm()
        context['status_form'] = MissionSpeakerStatusAnswerForm()

        return context
# ----------------------------------------------------------------------------------------------------------------







class IndividualMissionUpdateView(SpeakerStatuPassesTestMixin, UpdateView):
    '''Update an Individual Mission'''
    model = IndividualMission
    fields = ['name', 
            'field', 
            'level',
            'description',
            'acquired_skill',
            'due_date']
    template_name = 'crud/update.html'  


def get_object(self):
    pk = self.kwargs.get['pk']
    return get_object_or_404(IndividualMission, pk=pk)

# ----------------------------------------------------------------------------------------------------------------





class CollectiveMissionUpdateView(SpeakerStatuPassesTestMixin, UpdateView):
    '''Update a Collective Mission'''
    model = CollectiveMission
    fields = ['name',
            'field',
            'level',
            'description',
            'attributed_to']
    template_name = 'crud/update.html'


    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(CollectiveMission, pk=pk)

    def get_success_url(self):
        return reverse_lazy('collective_mission_detail', kwargs ={'pk': self.object.id})
# ----------------------------------------------------------------------------------------------------------------








class IndividualMissionDeleteView(SpeakerStatuPassesTestMixin, DeleteView):
    model = IndividualMission
    template_name = 'crud/delete.html' 
    success_url = reverse_lazy('project_list')


    def get_object(self, queryset=None):
        pk = self.kwargs['pk']
        return get_object_or_404(IndividualMission, pk=pk)
# ----------------------------------------------------------------------------------------------------------------


class CollectiveMissionDeleteView(SpeakerStatuPassesTestMixin, DeleteView):
    model = CollectiveMission
    template_name = 'crud/delete.html'
    success_url = reverse_lazy('project_list')


    def get_object(self, queryset=None):
        pk = self.kwargs['pk']
        return get_object_or_404(CollectiveMission, pk=pk)
# ----------------------------------------------------------------------------------------------------------------



class ClaimMission(ProfileCheckPassesTestMixin, RedirectView):
    ''' Own a mission -student'''
    # query_sting = False >>this is false by default     
    pattern_name = 'my_mission_list'

    def get_redirect_url(self,  *args, **kwargs):
        mission = get_object_or_404(IndividualMission, pk=kwargs['pk'])
        mission.attributed_to = self.request.user.profile()
        mission.save()
        del kwargs['pk']
        return super().get_redirect_url(*args, **kwargs)


# del pk >>because we dont need a PK so we cancel after we use it 

# ----------------------------------------------------------------------------------------------------------------




class UnclaimMission(StudentStatuPassesTestMixin, RedirectView):
    ''' Unclaim the mission - will return to the list of available Mission'''
    # query_sting = False >>this is false by default     
    pattern_name = 'my_mission_list'

    def get_redirect_url(self,  *args, **kwargs):
        mission = get_object_or_404(IndividualMission, pk=kwargs['pk'])
        mission.attributed_to = None
        mission.save()
        del kwargs['pk']
        return super().get_redirect_url(*args, **kwargs)


#
#
#
# class TeamCollectiveMissionDetailView(ProfileCheckPassesTestMixin, DetailView):
#     '''Here to create a team manager - gettinga project and managing participants '''
#
#     model = CollectiveMission
#     template_name = 'backend/mission/team_mission_detail.html'
#
#
#     def get_object(self):
#         pk = self.kwargs.get('pk')
#         return get_object_or_404(CollectiveMission, pk=pk)
#

# ----------------------------------------------------------------------------------------------------------------



# on the get contex data im adding  the context that I get in the page. here it mean that when I call this view ill get to add in the kward update 
# the view -template will get the update in an {% if update%}
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['update']= True
#         return context
#
#     def get_success_url(self):
#         return reverse_lazy('team_detail', kwargs ={'pk': self.object.project.team.id})
#
#     def form_valid(self, form):
#         print(form.errors)
#         return super().form_valid(form)

# ----------------------------------------------------------------------------------------------------------------






class JoinCollectiveMissionView(StudentStatuPassesTestMixin, RedirectView):

        pattern_name = 'collective_mission_detail'

        def get_redirect_url(self, *args, **kwargs):
            collective_mission = get_object_or_404(CollectiveMission, pk=kwargs['pk'])
            IndividualCollectiveMission.objects.get_or_create(parent_mission=collective_mission, attributed_to=self.request.user.profile())

            return super().get_redirect_url(*args, **kwargs)






# _________________________________________________________________________________________________________





class LeaveCollectiveMissionView(StudentStatuPassesTestMixin, RedirectView):
    pattern_name= 'collective_mission_detail'

    def get_redirect_url(self, *args, **kwargs):
        collective_mission = get_object_or_404(CollectiveMission, pk=kwargs['pk'])
        IndividualCollectiveMission.objects.get(parent_mission=collective_mission,
                                                          attributed_to=self.request.user.profile()).delete()
        print(collective_mission, "collective mission ")
        return super().get_redirect_url(*args, **kwargs)


# _________________________________________________________________________________________________________


def assign_mission(request, pk):

    collective_mission = get_object_or_404(CollectiveMission, pk=pk)
    team = collective_mission.project.team
    participants = collective_mission.project.team.participants.all()

    form = CollectiveMissionAssign(request.POST or None )
    form.fields['participants'].queryset = team.participants.all()
    if request.method == "POST":

        if form.is_valid():

            form.save_individuals(collective_mission)

            return redirect('collective_mission_detail', collective_mission.id)
        else:
            print(repr(form), 'form')
    return render(request, "crud/create.html", {'form': form})


def clean_bulk_mission(mission, projects):

    for project in projects:
        print('los projetctos', projects)
        mission.id=None
        mission.mission_ptr.id =None
        new_mission_ptr = mission.mission_ptr.save()
        mission.mission_ptr = new_mission_ptr
        mission.project = project
        mission.created_date = timezone.now()
        mission.due_date = timezone.now()
        mission.completed = False
        if mission.mission_type =='i':
            mission.attributed_to = None
            print("mission cleaned", mission)
            mission.save()
        mission.save()
    print("missions", )


def bulk_add_individual_mission(request, **kwargs):

    ''' Add bulk Mission in Project '''

    individual_form = IndividualMissionAddForm(request.POST)
    mission_bulk_form = BulkAddMissionForm(data=request.POST)

    if request.method == "POST":
        if individual_form.is_valid() and mission_bulk_form.is_valid():
            projects = mission_bulk_form.cleaned_data['projects']
            project = projects.first()
            print('project', project)
            mission = individual_form.save(commit=False)
            mission.owner = request.user
            mission.mission_type='i'
            mission.project =project
            mission.save()
            clean_bulk_mission(mission, projects.exclude(id=mission.project.id))


            print('*****mission_form***', mission)
            print('mission_id ***', mission.id)

            print(f'mission for project {project}')


            return redirect('individual_mission_detail', mission.id)

    return render(request, 'backend/project/project_list.html', {'individual_form':individual_form,'mission_bulk_form': mission_bulk_form})






def bulk_add_collective_mission(request, *kwargs):
    ''' Add bulk Mission in Project '''

    collective_form = CollectiveMissionAddForm()
    mission_bulk_form = BulkAddMissionForm(request.POST)
    projects= mission_bulk_form.cleaned_data['projects']
    print(projects)
    if request.method == "POST":
        if collective_form.is_valid() and mission_bulk_form.is_valid():
            mission = mission_bulk_form.save(commit=False)
            mission_form = collective_form.save(commit=False)
            mission.id = None
            mission.mission_type = mission_bulk_form.cleaned_data['mission_type']
            mission.owner = request.user
            projects = mission_bulk_form.cleaned_data['projects'].filter(speaker=request.user)
            for project in projects:
                mission.project_id = project.id

            del kwargs['pk']
            print(f'mission for project {project}', mission)
            mission.save()

        return redirect('individual_mission_detail', mission.id)

    return render(request, 'backend/mission/mission_detail.html', {'mission_bulk_form': mission_bulk_form})





# ______________________SPEAKAER____VALIDATION _______________________________________________________________________________



def validate_mission(request, form):
    mission  = get_object_or_404(IndividualMission, pk=pk)
    form = ValidateMissionForm(request.POST)
    print(request.POST)
    if request.method == "POST":
        print("vlaide")
        if form.is_valid():
            form.attributed_to = mission.attributed_to
            form.save(validate_mission)
            return redirect('answer_mission_list')
        else:
            print("not validate")

    return render(request, "backend/mission/my_mission_list.html", {'form': form})



class ValidateMission(SpeakerStatuPassesTestMixin, RedirectView):
    ''' ValidateMission a mission of-student'''
    pattern_name = 'my_mission_list'

    def get_redirect_url(self, *args, **kwargs):
        mission = get_object_or_404(IndividualMission, pk=kwargs['pk'])
        mission.accepted = True
        mission.save()
        return super().get_redirect_url(*args, **kwargs)

