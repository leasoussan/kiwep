from django.shortcuts import render, get_object_or_404
from .models import Project
from django.forms import ModelForm
from .forms import ProjectAddForm
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
from accounts.mixin import ProfileCheckPassesTestMixin, SpeakerStatuPassesTestMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

# -------------------PROJECT---List_View/

class ProjectListView(LoginRequiredMixin, ProfileCheckPassesTestMixin, ListView):
    model = Project
    template_name = 'backend/project/project_list.html'
    context_object_name = 'project_list'

    




# ----------------PROJECT------Detail_View/

class ProjectDetailView(LoginRequiredMixin,ProfileCheckPassesTestMixin, DetailView):
    model = Project
    template_name = 'backend/project/project_detail.html'
    
    def get_object(self):
        pk = self.kwargs.get("pk")
        return get_object_or_404(Project, pk=pk)




# -----------------------------PROJECT-----Create_View:


class ProjectCreatelView(SuccessMessageMixin, LoginRequiredMixin, SpeakerStatuPassesTestMixin, CreateView):
    model = Project
    form_class = ProjectAddForm
    template_name = 'crud/create.html'
    success_message = "Your project was created successfuly"
    # formset = ProjectMissionFormSet()

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.speaker = self.request.user.profile()
        self.object.completed = False
        self.object.save()

        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'You have an error in your form')
        return super().form_invalid(form)


# To Overwrite the Get_absolut_url if I want it to go somewhere else - for ex in the update view 

    # def get_success_url(self):
    #     return ('content/project_list')


# -----------------------------PROJECT-----UpdateView:


class ProjectUpdateView(LoginRequiredMixin, SpeakerStatuPassesTestMixin, UpdateView):
    model = Project
    fields = ['name',
            'description',
            'time_to_complet',
            'field',
            'difficulty',
            'missions']
    template_name = 'crud/update.html'
    
    def get_object(self):
        pk = self.kwargs.get("pk")
        return get_object_or_404(Project, pk=pk)

    def form_valid(self,form):
        return super().form_valid(form)



# 
# -----------------------------PROJECT-----:Delete View 

class ProjectDeleteView(LoginRequiredMixin, SpeakerStatuPassesTestMixin, DeleteView):
    model = Project
    template_name = 'crud/delete.html'
    success_url = reverse_lazy('project_list')

    def get_object(self):
        pk = self.kwargs.get("pk")
        return get_object_or_404(Project, pk=pk)


# author = Project.objects.get(name=)
# formset = BookFormSet(instance=author)