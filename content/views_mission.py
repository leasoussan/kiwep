from django.shortcuts import render, get_object_or_404
from .models import Mission
from django.forms import ModelForm
from .forms import MissionAddForm
from django.urls import reverse_lazy


from django.views.generic import (
    CreateView, 
    DetailView, 
    ListView, 
    DetailView, 
    UpdateView, 
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.mixin import ProfileCheckPassesTestMixin



class MissionListView(LoginRequiredMixin,ProfileCheckPassesTestMixin, ListView):
    model = Mission
    template_name = 'crud/mission/mission_list.html'    
    context_object_name = 'mission_list'






class MissionDetailView(LoginRequiredMixin,ProfileCheckPassesTestMixin, DetailView):
    model = Mission
    template_name = 'crud/mission/mission_detail.html'    
    

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Mission, pk=pk)




class MissionCreateView(LoginRequiredMixin, ProfileCheckPassesTestMixin, CreateView):
    model = Mission
    form_class = MissionAddForm 
    template_name = 'crud/mission/mission_create.html'  


    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.speaker = self.request.user
        self.object.save()
        return super().form_valid(form)


class MissionUpdateView(LoginRequiredMixin,ProfileCheckPassesTestMixin, UpdateView):
    model = Mission
    fileds = ['name', 
            'field', 
            'level',
            'description',
            'completed',
            'resources',]
    template_name = 'crud/mission/mission_create.html'  


class MissionDeleteView(LoginRequiredMixin,ProfileCheckPassesTestMixin, DeleteView):
    model = Mission
    template_name = 'crud/mission/mission_delete.html' 
    success_url = reverse_lazy('mission_list')