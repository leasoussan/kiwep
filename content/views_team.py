from django.shortcuts import render, get_object_or_404
from .models import Team
from django.forms import ModelForm
from .forms import ProjectAddForm, TeamAddForm
from django.urls import reverse_lazy


from django.views.generic import (
    CreateView, 
    DetailView, 
    ListView, 
    DetailView, 
    UpdateView, 
    DeleteView
)



class TeamListView(ListView):
    model = Team
    template_name = 'content/team_list.html'
    context_object_name = 'team_list'



class TeamDetailView(DetailView):
    model = Team
    template_name = 'content/team_detail.html'

    def get_object(self):
        pk = self.kwargs.get("pk")
        return get_object_or_404(Team, pk=pk)


class TeamCreatelView(CreateView):
    model = Team 
    form_class = TeamAddForm
    template_name = 'content/team/team_create.html'
    


class TeamUpdateView(UpdateView):
    model = Team 
    field = ['name', 'project', 'start_date', 'due_date', 'group_Institution', 'participants', 'tasks' ,'final_project'] 
    template_name = 'content/team/team_edit.html'
    success_url = ('team_detail')

    def form_valid(self,form):
        return super().form_valid(form)



class TeamDeleteView(DeleteView):
    model = Team
    template_name = 'content/team_delete.html'
    success_url = reverse_lazy('team_list')

    def get_object(self):
        pk = self.kwargs.get("pk")
        return get_object_or_404(Project, pk=pk)