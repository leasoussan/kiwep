from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, HttpResponse,redirect
from .models import Resource
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


class ResourceListView(ProfileCheckPassesTestMixin, ListView):
    model = Resource
    template_name = 'backend/resource/resource_list.html'
    context_object_name = 'resource_list'

    #
    # def get_queryset(self):
    #     return super().get_queryset().filter(project__resource__in= self.project_)
    #


class ResourceDetailView(ProfileCheckPassesTestMixin, DetailView):

    model = Resource
    template_name = 'backend/resource/resource_detail.html'

    def get_object(self):
        pk = self.kwargs.get('pk') 
        return get_object_or_404(Resource, pk=pk)




class ResourceCreateView(LoginRequiredMixin, SpeakerStatuPassesTestMixin, CreateView):
     
    model = Resource
    form_class = ResourceAddForm
    template_name = 'crud/create.html'


    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)





class ResourceUpdateView(LoginRequiredMixin, SpeakerStatuPassesTestMixin, UpdateView):
    model = Resource
    template_name = 'crud/update.html'
    fields = ['name', 
            'link',
            'text',
            'image']
    # success_url = ('resource_detail')

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Resource, pk=pk)


class ResourceDeleteView(LoginRequiredMixin, SpeakerStatuPassesTestMixin, DeleteView):
    model = Resource
    template_name = 'crud/delete.html'
    success_url = reverse_lazy('resource_list')

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Resource, pk=pk)