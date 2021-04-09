from django.shortcuts import render, redirect, get_object_or_404
from .models import Team, TeamProjectMission, Project, Mission
from django.forms import ModelForm
from .forms import TeamAddForm, TeamProjectMissionFormSet, AddMemberTeamForm
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



class TeamListView(LoginRequiredMixin, ProfileCheckPassesTestMixin, ListView):
    model = Team
    template_name = 'crud/list_view.html'
    context_object_name = 'team_list'








class TeamDetailView(LoginRequiredMixin, ProfileCheckPassesTestMixin, DetailView):
    model = Team
    template_name = 'backend/team/team_detail.html'
    queryset = TeamProjectMission.objects.team_available_mission()


    def get_object(self):
        pk = self.kwargs.get("pk")
        return get_object_or_404(Team, pk=pk)








class TeamCreateView(LoginRequiredMixin, SpeakerStatuPassesTestMixin,  CreateView):
    model = Team 
    form_class = TeamAddForm
    template_name = 'crud/create.html'
    


    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.manager = self.request.user.profile()
        self.object.completed = False
        self.object.save()

        return super().form_valid(form)

    
    def get_success_url(self):
        return reverse_lazy('create_team_missions', kwargs={'pk':self.object.id})










class TeamCreateMissionView(LoginRequiredMixin, SpeakerStatuPassesTestMixin, View):
    model = TeamProjectMission
    def get(self, request, *args, **kwargs):
        
        team = Team.objects.get(id = self.kwargs['pk'])
        missions = team.project.mission.all()
        participants= team.participants.all()
        initial_data = [{'mission': mission.id} for mission in missions ]
        formset = TeamProjectMissionFormSet(instance = team, initial = initial_data)
        
        for form in formset:

            form.fields['attributed_to'].queryset = participants
                       

        return render(request, 'crud/create_team_missions.html', {'formset': formset})
    

    def post(self, request, *args, **kwargs):
        
        team = Team.objects.get(id = self.kwargs['pk'])
        missions = team.project.mission.all()
        
        formset = TeamProjectMissionFormSet(request.POST, instance = team)

        
        if formset.is_valid():
            formset.save()
            return redirect('team_detail' , team.id)

        
        for form in formset:
            form.fields['mission'].queryset = missions
           
        return render(request, 'crud/create_team_missions.html', {'formset': formset})









class TeamUpdateView(LoginRequiredMixin, SpeakerStatuPassesTestMixin, UpdateView):
    model = Team 
    fields = ['name', 'project', 'start_date', 'due_date', 'group_Institution', 'participants', 'tasks' ,'final_project'] 
    template_name = 'crud/update.html'
    success_url = ('team_detail')


    def form_valid(self,form):
        return super().form_valid(form)








class TeamDeleteView(LoginRequiredMixin, SpeakerStatuPassesTestMixin, DeleteView):
    model = Team
    template_name = 'crud/delete.html'
    success_url = reverse_lazy('team_list')

    def get_object(self):
        pk = self.kwargs.get("pk")
        return get_object_or_404(Team, pk=pk)












class JoinTeamView(LoginRequiredMixin, RedirectView):
    pattern_name = 'team_detail'


    def get_redirect_url(self, *args, **kwargs):
        team = get_object_or_404(Team, pk=kwargs['pk'])
        team.participants.add(self.request.user.profile())
        
        return super().get_redirect_url(*args, **kwargs)
  




class AddTeamMemberView(LoginRequiredMixin, UpdateView):
    model = Team 
    template_name = 'crud/update.html'
    success_url = ('team_detail')
    form_class = AddMemberTeamForm

    def get_success_url(self):
        return reverse_lazy('team_detail', kwargs={'pk': self.object.id})

    def form_invalid(self, form):
        print("error")
        print(form.errors)
        return super().form_invalid(form)