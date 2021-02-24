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



# -------------------PROJECT---List_View/

class ProjectListView(ListView):
    model = Project
    template_name = 'content/project/project_list.html'
    context_object_name = 'project_list'

    def get_queryset(self):
        return Project.objects.filter(speaker=self.request.user.profile)




# ----------------PROJECT------Detail_View/

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'content/project/project_detail.html'
    
    def get_object(self):
        pk = self.kwargs.get("pk")
        return get_object_or_404(Project, pk=pk)




# -----------------------------PROJECT-----Create_View:


class ProjectCreatelView(CreateView):
    model = Project
    form_class = ProjectAddForm
    template_name = 'content/project/project_create.html'

    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.speaker = self.request.user
        self.object.completed = False
        self.object.save()
        return super().form_valid(form)

# To Overwrite the Get_absolut_url if I want it to go somewhere else - for ex in the update view 

    # def get_success_url(self):
    #     return ('content/project_list')


# -----------------------------PROJECT-----UpdateView:


class ProjectUpdateView(UpdateView):
    model = Project
    fields = ['name',
            'description',
            'time_to_complet',
            'field',
            'difficulty',
            'mission']
    template_name = 'content/update_project.html'
    
    def get_object(self):
        pk = self.kwargs.get("pk")
        return get_object_or_404(Project, pk=pk)

    def form_valid(self,form):
        return super().form_valid(form)



# 
# -----------------------------PROJECT-----:Delete View 

class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'content/delete_project.html'
    success_url = reverse_lazy('project_list')

    def get_object(self):
        pk = self.kwargs.get("pk")
        return get_object_or_404(Project, pk=pk)
