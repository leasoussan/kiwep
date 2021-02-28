from django.shortcuts import render, get_object_or_404
from .models import Resource
from django.forms import ModelForm
from .forms import ResourceAddForm
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
from accounts.mixin import ProfileCheckPassesTestMixin


class ResourceListView(LoginRequiredMixin, ProfileCheckPassesTestMixin, ListView):
    model = Resource
    template_name = 'content/resource/resource_list.html'
    context_object_name = 'resource_list'



class ResourceDetailView(LoginRequiredMixin, ProfileCheckPassesTestMixin, DetailView):

    model = Resource
    template_name = 'content/resource/resource_detail.html'

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Resource, pk=pk)




class ResourceCreateView(LoginRequiredMixin, ProfileCheckPassesTestMixin, CreateView):
     
    model = Resource
    form_class = ResourceAddForm
    template_name = 'content/resource/resource_create.html'


    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.speaker = self.request.user
        self.object.save()
        return super().form_valid(form)



class ResourceUpdateView(LoginRequiredMixin, ProfileCheckPassesTestMixin, UpdateView):
    model = Resource
    template_name = 'content/resource/resource_update.html'
    fields = ['name', 
            'link',
            'text',]
    success_url = ('resource_detail')

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Resource, pk=pk)


class ResourceDeleteView(LoginRequiredMixin, ProfileCheckPassesTestMixin, DeleteView):
    model = Resource
    template_name = 'content/resource/resource_delete.html'
    success_url = reverse_lazy('resource_list')

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Resource, pk=pk)