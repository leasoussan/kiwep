from django.shortcuts import render, redirect, get_object_or_404
from .models import Team, TeamProjectMission, Project
from django.forms import ModelForm
from .forms import TeamAddForm, TeamProjectMissionFormSet
from django.urls import reverse_lazy


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


class TeamCreateView(LoginRequiredMixin, ProfileCheckPassesTestMixin,  CreateView):
    model = Team 
    form_class = TeamAddForm
    template_name = 'crud/create.html'
    
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs) 
    #     context['formset']= TeamProjectMissionFormSet(self.request.POST or None)
    #     return context


    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.manager = self.request.user.profile()
        self.object.completed = False
        self.object.save()

        # formset = TeamProjectMissionFormSet(self.request.POST, instance = self.object)
        
        # if formset.is_valid():
        #     formset.save()
        #     return super().form_valid(form)
        return super().form_valid(form)

    
    def get_success_url(self):
        return reverse_lazy('create_team_missions', kwargs={'id':self.object.id})





class TeamCreateMissionView(LoginRequiredMixin, ProfileCheckPassesTestMixin, View):
    model = TeamProjectMission
    def get(self, request, *args, **kwargs):
        
        team = Team.objects.get(id = self.kwargs['id'])
        missions = team.project.mission.all()
        student = team.participants.all()
        formset = TeamProjectMissionFormSet(instance = team)
        
        for form in formset:
            form.fields['mission'].queryset = missions
            form.fields['attributed_to'].queryset = student

        return render(request, 'crud/create_team_missions.html', {'formset': formset})
    

    def post(self, request, *args, **kwargs):
        
        team = Team.objects.get(id = self.kwargs['id'])
        missions = team.project.mission.all()
        student = team.participants.all()
        formset = TeamProjectMissionFormSet(request.POST, instance = team)


        if formset.is_valid():
            formset.save()
            return redirect('team_list')
        return render(request, 'crud/create_team_missions.html', {'formset': formset})





# class TeamCreateView(LoginRequiredMixin, ProfileCheckPassesTestMixin, CreateView):
#     model = Team 
#     form_class = TeamAddForm
#     template_name = 'crud/create.html'
    

#     def form_valid(self, form):
#         self.object = form.save(commit = False)
#         self.object.manager = self.request.user.profile()
#         self.object.save()
        
#         # return super().form_valid(form)
#         return redirect('create_team_missions', form.cleaned_data['team.id'])




# # def get_context_data(self):
# #         # allo to access the team with the team ID 
# #         # team = team.object.get(id - team_id)
# #         # when initialising formset = intance = team
# #         pass


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