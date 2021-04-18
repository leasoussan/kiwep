from django.shortcuts import render, get_object_or_404
from .models import Mission, CollectiveProjectMission, Team
from django.forms import ModelForm
from .forms import MissionAddForm, SubmitMissionForm
from django.urls import reverse_lazy
from django.views.generic.base import RedirectView

from django.views.generic import (
    CreateView, 
    DetailView, 
    ListView, 
    DetailView, 
    UpdateView, 
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.mixin import ProfileCheckPassesTestMixin, SpeakerStatuPassesTestMixin



class MissionListView(LoginRequiredMixin,ProfileCheckPassesTestMixin, ListView):
    ''' To See all Missions View'''
    model = CollectiveProjectMission
    template_name = 'content/mission/mission_list.html'    
    context_object_name = 'mission_list'


    # def get_queryset(self):
    #     return super().get_queryset().filter(attributed_to = self.request.user.profile())


class MyMissionList(LoginRequiredMixin,ProfileCheckPassesTestMixin, ListView):
    ''' See User Missions List'''
    model = CollectiveProjectMission
    template_name = 'backend/mission/my_mission_list.html'    
    context_object_name = 'my_mission_list'


    def get_queryset(self):
        return super().get_queryset().filter(attributed_to = self.request.user.profile())



class MissionDetailView(LoginRequiredMixin,ProfileCheckPassesTestMixin, DetailView):
    '''Detail Of General Mission'''
    model = Mission
    template_name = 'backend/mission/mission_detail.html'    
    

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Mission, pk=pk)




class MissionCreateView(LoginRequiredMixin, SpeakerStatuPassesTestMixin, CreateView):
    ''' Create Mission - Will Go into General Mission'''
    model = Mission
    form_class = MissionAddForm 
    template_name = 'crud/create.html'  


    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)




class MissionUpdateView(LoginRequiredMixin,SpeakerStatuPassesTestMixin, UpdateView):
    '''Update a Mission'''
    model = Mission
    fields = ['name', 
            'field', 
            'level',
            'description',
            'resources',]
    template_name = 'crud/update.html'  


def get_object(self):
    pk = self.kwargs.get['pk']
    return get_object_or_404(Mission, pk =pk)


class MissionDeleteView(LoginRequiredMixin,SpeakerStatuPassesTestMixin, DeleteView):
    model = Mission
    template_name = 'crud/delete.html' 
    success_url = reverse_lazy('mission_list')





class ClaimMission(LoginRequiredMixin, RedirectView):
    ''' Own a mission -student'''
    # query_sting = False >>this is false by default     
    pattern_name = 'my_mission_list'

    def get_redirect_url(self,  *args, **kwargs):
        mission = get_object_or_404(CollectiveProjectMission, pk=kwargs['pk'])
        mission.attributed_to = self.request.user.profile()
        mission.save()
        del kwargs['pk']
        return super().get_redirect_url(*args, **kwargs)


# del pk >>because we dont need a PK so we cancel after we use it 



class UnclaimMission(LoginRequiredMixin, RedirectView):
    ''' Unclaim the mission - willr eturn to the list of available Mission'''
    # query_sting = False >>this is false by default     
    pattern_name = 'my_mission_list'

    def get_redirect_url(self,  *args, **kwargs):
        mission = get_object_or_404(CollectiveProjectMission, pk=kwargs['pk'])
        mission.attributed_to = None
        mission.save()
        del kwargs['pk']
        return super().get_redirect_url(*args, **kwargs)





class TeamMissionDetailView(LoginRequiredMixin,ProfileCheckPassesTestMixin, DetailView):
    '''Here to create a team manager - gettinga project and managing participants '''

    model = CollectiveProjectMission
    template_name = 'backend/mission/team_mission_detail.html'    
    

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(CollectiveProjectMission, pk=pk)





class StudentSubmitMission(UpdateView):
    ''' An answer can be saved and unsubmited- here is the submit  '''
    model = CollectiveProjectMission
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
