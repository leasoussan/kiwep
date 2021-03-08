from django.shortcuts import render, get_object_or_404
from .models import Team
from django.forms import ModelForm
from .forms import TeamAddForm
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



class TeamListView(LoginRequiredMixin, ProfileCheckPassesTestMixin, ListView):
    model = Team
    template_name = 'crud/list_view.html'
    context_object_name = 'team_list'



class TeamDetailView(LoginRequiredMixin, ProfileCheckPassesTestMixin, DetailView):
    model = Team
    template_name = 'crud/detail_view.html'

    def get_object(self):
        pk = self.kwargs.get("pk")
        return get_object_or_404(Team, pk=pk)


class TeamCreateView(LoginRequiredMixin, ProfileCheckPassesTestMixin, CreateView):
    model = Team 
    form_class = TeamAddForm
    template_name = 'crud/create.html'


    def form_valid(self, form):
        self.object = form.save(commit = False)
        self.object.manager = self.request.user.profile()

        self.object.save()
        
        return super().form_valid(form)


class TeamUpdateView(LoginRequiredMixin, ProfileCheckPassesTestMixin, UpdateView):
    model = Team 
    field = ['name', 'project', 'start_date', 'due_date', 'group_Institution', 'participants', 'tasks' ,'final_project'] 
    template_name = 'crud/update.html'
    success_url = ('team_detail')


    def form_valid(self,form):
        return super().form_valid(form)



class TeamDeleteView(LoginRequiredMixin, ProfileCheckPassesTestMixin, DeleteView):
    model = Team
    template_name = 'crud/delete.html'
    success_url = reverse_lazy('team_list')

    def get_object(self):
        pk = self.kwargs.get("pk")
        return get_object_or_404(Team, pk=pk)