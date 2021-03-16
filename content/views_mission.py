from django.shortcuts import render, get_object_or_404
from .models import Mission, TeamProjectMission
from django.forms import ModelForm
from .forms import MissionAddForm
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
    model = TeamProjectMission
    template_name = 'crud/list_view.html'    
    context_object_name = 'mission_list'


    # def get_queryset(self):
    #     return super().get_queryset().filter(attributed_to = self.request.user.profile())





class MissionDetailView(LoginRequiredMixin,ProfileCheckPassesTestMixin, DetailView):
    model = Mission
    template_name = 'backend/mission/mission_detail.html'    
    

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Mission, pk=pk)




class MissionCreateView(LoginRequiredMixin, SpeakerStatuPassesTestMixin, CreateView):
    model = Mission
    form_class = MissionAddForm 
    template_name = 'crud/create.html'  


    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)




class MissionUpdateView(LoginRequiredMixin,SpeakerStatuPassesTestMixin, UpdateView):
    model = Mission
    fileds = ['name', 
            'field', 
            'level',
            'description',
            'completed',
            'resources',]
    template_name = 'crud/update.html'  


class MissionDeleteView(LoginRequiredMixin,SpeakerStatuPassesTestMixin, DeleteView):
    model = Mission
    template_name = 'crud/delete.html' 
    success_url = reverse_lazy('mission_list')





class ClaimMission(LoginRequiredMixin, RedirectView):
    # query_sting = False >>this is false by default     
    pattern_name = 'mission_list'

    def get_redirect_url(self,  *args, **kwargs):
        mission = get_object_or_404(TeamProjectMission, pk=kwargs['pk'])
        mission.attributed_to = self.request.user.profile()
        mission.save()
        del kwargs['pk']
        return super().get_redirect_url(*args, **kwargs)


# del pk >>because we dont need a PK so we cancel after we use it 

