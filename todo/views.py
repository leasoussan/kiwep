from django.shortcuts import render, get_object_or_404
from .models import *
from django.views.generic import CreateView, ListView, DetailView
from accounts.mixin import SpeakerStatuPassesTestMixin, ProfileCheckPassesTestMixin
from .forms import AddPersonalTaskForm



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
class PersonalTaskDetailView(DetailView):
    model = PersonalTask
    template_name = "crud/detail_view.html"

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(PersonalTask, pk=pk)

class MyTasksView(ProfileCheckPassesTestMixin, ListView):
    model= PersonalTask
    template_name = 'todo/todo_list.html' 
    context_object_name = 'personal_task'



    def get_queryset(self):
        return super().get_queryset().filter(creator = self.request.user)




class TeamTaskCreateView(SpeakerStatuPassesTestMixin, CreateView):
    model = TeamTask
    template_name = "crud/create.html"
    
    fields = ['title','details','due_date', 'team']

    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.creator = self.request.user
        self.object.save()

        return super(CreateView, self).form_valid(form)


class TeamTaskDetailView(DetailView):
    model = TeamTask
    template_name = 'todo/todo_detail.html'
    context_object_name = 'team_tasks'




class AssignedTaskCreateView(SpeakerStatuPassesTestMixin, CreateView):
    model = AssignedTask
    template_name = "crud/create.html"
    fields = ['title','details','due_date', 'assignee']

    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.creator = self.request.user
        self.object.save()

        return super(CreateView, self).form_valid(form)