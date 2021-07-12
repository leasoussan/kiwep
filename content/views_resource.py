from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, HttpResponse,redirect
from django.views import View

from .models import Resource, Project
from django.forms import ModelForm
from .forms import ResourceAddForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import user_passes_test, login_required

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


class ProjectResourceListView(ProfileCheckPassesTestMixin, ListView):
    model = Resource
    template_name = 'backend/resource/resource_list.html'
    context_object_name = 'resource_list'

    def get_queryset(self):
        pk = self.kwargs.get['pk']
        return Resource.objects.filter(project__id = pk)



class ResourceDetailView(ProfileCheckPassesTestMixin, DetailView):

    model = Resource
    template_name = 'backend/resource/resource_detail.html'

    def get_object(self):
        pk = self.kwargs.get('pk')
        project = Project.objects.get(id=self.kwargs['project_id'])
        print('project', project.id)
        print('pk', pk)
        return get_object_or_404(Resource, pk=pk)




class ResourceCreateView(LoginRequiredMixin, SpeakerStatuPassesTestMixin, View):
     

    def get(self, request, *args, **kwargs):
        project = Project.objects.get(id=self.kwargs['project_id'])
        form = ResourceAddForm()
        return render(request, 'crud/create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        project = Project.objects.get(id=self.kwargs['project_id'])
        form = ResourceAddForm(request.POST, request.FILES,)

        if request.method == "POST":
            if form.is_valid():
                resource = form.save(commit =False)
                print(resource)
                resource.owner = self.request.user
                resource.save()
                project.resources.add(resource)
                print('your resource was saved"', project.id)

            return redirect('project_detail', project.id)

        return render(request, 'crud/create.html', {'form': form})






class ResourceUpdateView(LoginRequiredMixin, SpeakerStatuPassesTestMixin, UpdateView):
    model = Resource
    template_name = 'crud/update.html'
    fields = ['name', 
            'link',
            'text',
            'image']


    def get_object(self):

        project = Project.objects.get(id=self.kwargs['project_id'])
        pk = self.kwargs.get('pk')
        print('project', project.id)
        print('pk', pk)
        return get_object_or_404(Resource, pk=pk, project=project)

    def get_success_url(self):
        return reverse_lazy('resource_detail', kwargs={'pk': self.object.id, 'project_id':self.project.id})


class ResourceDeleteView(LoginRequiredMixin, SpeakerStatuPassesTestMixin, DeleteView):
    model = Resource
    template_name = 'crud/delete.html'
    success_url = reverse_lazy('resource_list')

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Resource, pk=pk)