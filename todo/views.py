from django.shortcuts import render
from .models import *
from django.generic.views import CreateView 
from accounts.mixin import SpeakerStatuPassesTestMixin, 

class PersonalTaskCreateView(ProfileCheckPassesTestMixin, CreateView):
    model = PersonalTask
    template_name = "crud/create.html"
    fields = ['title','details','due_date']

    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.creator = self.request.user
        self.object.save()

        return super(CreateView, self).form_valid(form)

# in the return we are calling the super of CRETAE VIEW -GENERAL (not to hit the createview of PersnalTask)
# 

class TeamTaskCreateView(SpeakerStatuPassesTestMixin, CreateView):
    model = TeamTask
    template_name = "crud/create.html"
    fields = ['title','details','due_date', 'team']

    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.creator = self.request.user
        self.object.save()

        return super(CreateView, self).form_valid(form)



class AssignedTaskCreateView(SpeakerStatuPassesTestMixin, CreateView):
    model = AssignedTask
    template_name = "crud/create.html"
    fields = ['title','details','due_date', 'assignee']

    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.creator = self.request.user
        self.object.save()

        return super(CreateView, self).form_valid(form)