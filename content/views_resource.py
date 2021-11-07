from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, HttpResponse,redirect
from django.views import View

from .models import Resource, Project, Mission
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
    DeleteView, RedirectView
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
        print('pk', pk)
        return get_object_or_404(Resource, pk=pk)



class ResourceProjectCreateView(LoginRequiredMixin, SpeakerStatuPassesTestMixin, View):

    def get(self, request, *args, **kwargs):
        form = ResourceAddForm()
        return render(request, 'crud/create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        project = Project.objects.get(id=self.kwargs['project_id'])

        form = ResourceAddForm(request.POST, request.FILES,)

        if request.method == "POST":

            if form.is_valid():
                resource = form.save(commit =False)
                print(resource)
                resource.project = project
                resource.owner = self.request.user
                resource.save()
                print('your resource was saved to"', project.id)

            return redirect('project_detail', project.id)

        return render(request, 'crud/create.html', {'form': form})




class ResourceMissionCreateView(LoginRequiredMixin, SpeakerStatuPassesTestMixin, View):
    def get(self, request, *args, **kwargs):
        form = ResourceAddForm()

    def post(self, request, *args, **kwargs):
        mission = Mission.objects.get(id=self.kwargs['mission_id'])
        form = ResourceAddForm(request.POST, request.FILES,)

        if request.method == "POST":
            if form.is_valid():
                resource =form.save(commit=False)
                resource.project = mission.project
                print('project', mission.project)
                resource.mission = mission
                resource.owner=self.request.user
                resource.save()
                print('your resource was saved to"', mission.id)

            return redirect('resource_detail', resource.id)

        return render(request, 'crud/create.html', {'form': form})





def chose_resource_to_mission(request, mission, project):
    resources = project.resource_set.all()




class ResourceUpdateView(LoginRequiredMixin, SpeakerStatuPassesTestMixin, UpdateView):
    model = Resource
    template_name = 'crud/update.html'
    fields = ['name',
              'link',
              'text',
              'image',
              'file_rsc',
              ]


    def get_object(self):
        pk = self.kwargs.get('pk')
        print('pk', pk)
        return get_object_or_404(Resource, pk=pk)

    def get_success_url(self):
        return reverse_lazy('resource_detail', kwargs={'pk': self.object.id})



class ResourceDeleteView(LoginRequiredMixin, SpeakerStatuPassesTestMixin, DeleteView):
    model = Resource
    template_name = 'crud/delete.html'
    success_url = reverse_lazy('project_list')

    def get_object(self):
        pk = self.kwargs.get('pk')
        print('pk', pk)
        return get_object_or_404(Resource, pk=pk)

# # {TODO}
#     def get_context_data(self, **kwargs):
#         pass
#
#     def get_success_url(self):
#         return reverse_lazy('project_detail', kwargs={'pk': self.object.id})