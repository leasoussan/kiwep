from django.shortcuts import render, get_object_or_404, redirect
from .models import Mission, CollectiveMission, Team, IndividualMission, IndividualCollectiveMission
from django.forms import ModelForm
from .forms import MissionAddForm, SubmitMissionForm, IndividualMissionAddForm, CollectiveMissionAddForm, CollectiveMissionAssign, ValidateMissionForm
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
        return super().get_queryset().filter(attributed_to = self.request.user.profile())


# ----------------------------------------------------------------------------------------------------------------

class AnswerBoardMissionListView(ProfileCheckPassesTestMixin, ListView):
    ''' To See all Missions View'''
    model = IndividualMission
    template_name = 'backend/mission/my_mission_list.html'
    context_object_name = 'answers_mission_list'
    form = ValidateMissionForm()

    def get_queryset(self):
        return super().get_queryset().filter(attributed_to = True)

# ----------------------------------------------------------------------------------------------------------------



class AddIndividualMissionView(SpeakerStatuPassesTestMixin, View):

    ''' Add an Individual Mission '''
    model = IndividualMission

    def get(self, request, *args, **kwargs):
        return redirect('homepage')

    def post(self, request, *args, **kwargs):
        form = IndividualMissionAddForm(request.POST)

        if form.is_valid():
            mission = form.save(commit=False)
            mission.project_id= kwargs['project_id']
            mission.owner = self.request.user
            mission.save()
        return redirect('project_detail', kwargs['project_id'])


# ----------------------------------------------------------------------------------------------------------------






class AddCollectiveMissionView(SpeakerStatuPassesTestMixin, View):
    ''' See User Missions List'''
    model = CollectiveMission

    def get(self, request, *args, **kwargs):
        return redirect('homepage')

    def post(self, request, *args, **kwargs):
        form = CollectiveMissionAddForm(request.POST)

        if form.is_valid():
            collective_mission = form.save(commit=False)
            collective_mission.project_id = kwargs['project_id']
            collective_mission.owner = self.request.user
            collective_mission.save()

        return redirect('project_detail', kwargs['project_id'])








# ----------------------------------------------------------------------------------------------------------------

class IndividualMissionDetailView(ProfileCheckPassesTestMixin, DetailView):
    '''Detail Of General Mission'''
    model = IndividualMission
    template_name = 'backend/mission/mission_detail.html'    
    
    

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(IndividualMission, pk=pk)


# ----------------------------------------------------------------------------------------------------------------





class CollectiveMissionDetailView(ProfileCheckPassesTestMixin, DetailView):
    '''Detail Of General Mission'''
    model = CollectiveMission
    template_name = 'backend/mission/mission_detail.html'

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(CollectiveMission, pk=pk)


# ----------------------------------------------------------------------------------------------------------------







class IndividualMissionUpdateView(SpeakerStatuPassesTestMixin, UpdateView):
    '''Update an Individual Mission'''
    model = IndividualMission
    fields = ['name', 
            'field', 
            'level',
            'description',
            'resources',]
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
            'resources',
            'attributed_to']
    template_name = 'crud/update.html'


    def get_object(self):
        pk = self.kwargs.get['pk']
        return get_object_or_404(CollectiveMission, pk=pk)

# ----------------------------------------------------------------------------------------------------------------








class MissionDeleteView(SpeakerStatuPassesTestMixin, DeleteView):
    model = Mission
    template_name = 'crud/delete.html' 
    success_url = reverse_lazy('mission_list')


    def get_object(self, queryset=None):
        pk = self.kwargs.get['pk']
        return get_object_or_404(Mission, pk=pk)
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






class StudentSubmitMission(StudentStatuPassesTestMixin, UpdateView):

    ''' An answer can be saved and unsubmited- here is the submit  '''
    model = IndividualMission
    form_class = SubmitMissionForm
    # fields = [
    #         'response_comment',
    #         'response_file',
    #     ]
    template_name = 'backend/mission/mission_detail.html'


# on the get contex data im adding  the context that I get in the page. here it mean that when I call this view ill get to add in the kward update 
# the view -template will get the update in an {% if update%}
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['update']= True 
        return context

    def get_success_url(self):
        return reverse_lazy('team_detail', kwargs ={'pk': self.object.project.team.id})

    def form_valid(self, form):
        print(form.errors)
        return super().form_valid(form)

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

    # -------------------------------------------------------

    # class AssignCollectiveMissionView(SpeakerStatuPassesTestMixin, FormView):
    #     model = CollectiveMission
    #     form_class = CollectiveMissionAssign
    #     success_url = 'collective_mission_detail'
    #     template_name = "crud/create.html"
    #
    #     def get_object(self):
    #         pk = self.kwargs.get('pk')
    #         print(pk, "pk print")
    #         return get_object_or_404(CollectiveMission, pk=pk)
    #
    #     def get_form_kwargs(self):
    #         """Return the keyword arguments for instantiating the form."""
    #         collective_mission = self.get_object()
    #         kwargs = super().get_form_kwargs()
    #         kwargs['team'] = collective_mission.project.team
    #         kwargs['participants'] = collective_mission.project.team.participants.all()
    #         # if self.request.method == "POST":
    #         #     del kwargs['participants']
    #         return kwargs
    #
    #     def form_valid(self, form):
    #         """If the form is valid, redirect to the supplied URL."""
    #         print(form.cleaned_data, 'cleaned_data')
    #         collective_mission = self.get_object()
    #         print(collective_mission, "HERREE")
    #
    #         form.save(collective_mission)
    #
    #         return super().form_valid(form)
    #
    #
    #     def form_invalid(self, form):
    #         print(form['participants'],  'my form errors')
    #
    #         return super().form_invalid(form)
    #



