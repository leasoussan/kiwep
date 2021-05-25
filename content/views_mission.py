from django.shortcuts import render, get_object_or_404, redirect
from .models import Mission, CollectiveMission, Team, IndividualMission
from django.forms import ModelForm
from .forms import MissionAddForm, SubmitMissionForm, IndividualMissionAddForm, CollectiveMissionAddForm
from django.urls import reverse_lazy
from django.views.generic.base import RedirectView

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



class IndividualMissionListView(ProfileCheckPassesTestMixin, ListView):
    ''' To See all Missions View'''
    model = IndividualMission
    template_name = 'backend/mission/my_mission_list.html'
    context_object_name = 'mission_list'


    def get_queryset(self):
        return super().get_queryset().filter(attributed_to = self.request.user.profile())


class AddIndividualMissionView(ProfileCheckPassesTestMixin, View):
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






class AddCollectiveMissionView(ProfileCheckPassesTestMixin, View):
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










class IndividualMissionDetailView(ProfileCheckPassesTestMixin, DetailView):
    '''Detail Of General Mission'''
    model = IndividualMission
    template_name = 'backend/mission/mission_detail.html'    
    
    

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(IndividualMission, pk=pk)





class CollectiveMissionDetailView(ProfileCheckPassesTestMixin, DetailView):
    '''Detail Of General Mission'''
    model = CollectiveMission
    template_name = 'backend/mission/mission_detail.html'

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(CollectiveMission, pk=pk)






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




class MissionDeleteView(SpeakerStatuPassesTestMixin, DeleteView):
    model = Mission
    template_name = 'crud/delete.html' 
    success_url = reverse_lazy('mission_list')





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



class UnclaimMission(ProfileCheckPassesTestMixin, RedirectView):
    ''' Unclaim the mission - will return to the list of available Mission'''
    # query_sting = False >>this is false by default     
    pattern_name = 'my_mission_list'

    def get_redirect_url(self,  *args, **kwargs):
        mission = get_object_or_404(IndividualMission, pk=kwargs['pk'])
        mission.attributed_to = None
        mission.save()
        del kwargs['pk']
        return super().get_redirect_url(*args, **kwargs)





class TeamMissionDetailView(ProfileCheckPassesTestMixin, DetailView):
    '''Here to create a team manager - gettinga project and managing participants '''

    model = CollectiveMission
    template_name = 'backend/mission/team_mission_detail.html'    
    

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(CollectiveMission, pk=pk)





class StudentSubmitMission(UpdateView):
    ''' An answer can be saved and unsubmited- here is the submit  '''
    model = CollectiveMission
    form_class = SubmitMissionForm
    # fields = [
    #         'response_comment',
    #         'response_file',
    #     ]
    template_name = 'backend/mission/team_mission_detail.html'


# on the get contex data im adding  the context that I get in the page. here it mean that when I call this view ill get to add in the kward update 
# the view -template will get the update in an {% if update%}
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['update']= True 
        return context

    def get_success_url(self):
        return reverse_lazy('team_detail', kwargs ={'pk': self.object.team.id})

    def form_valid(self, form):
        return super().form_valid(form)


