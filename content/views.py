from django.shortcuts import render, get_object_or_404
from .models import Project

from .forms import ProjectAddForm

from django.views.generic import (
    CreateView, 
    DetailView, 
    ListView, 
    DetailView, 
    UpdateView, 
    DeleteView
)





class ProjectListView(ListView):
    model = Project
    template_name = 'content/project_list.html'
    context_object_name = 'project_list'

    # Query Specifiq set of project
    # def get_queryset(self):
    #     return Project.objects.filter(created_by=self.request.user)


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'content/project_page.html'
    
    def get_object(self):
        pk = self.kwargs.get("pk")
        return get_object_or_404(Project, pk=pk)



class ProjectCreatelView(CreateView):
    model = Project
    form_class = ProjectAddForm
    template_name = 'content/create_project.html'

   

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.created_by = self.request.user
        self.object.save()
        return super().form_valid(form)

