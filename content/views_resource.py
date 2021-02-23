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


class ResourceListView(ListView):
    model = Resource
    template_name = 'content/resource/resource_list.html'
    context_object_name = 'resource_list'



class ResourceDetailView(DetailView):

    model = Resource
    template_name = 'content/resource/resource_detail.html'

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Resource, pk=pk)




class ResourceCreateView(CreateView):
     
    model = Resource
    form_class = ResourceAddForm
    template_name = 'content/resource/resource_create.html'


    def form_valid(self, form):
        return super().form_valid(form)




class ResourceUpdateView(UpdateView):
    model = Resource
    template_name = 'content/resource/resource_update.html'
    fields = ['name', 
            'link',
            'text',]
    success_url = ('resource_detail')

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Resource, pk=pk)


class ResourceDeleteView(DeleteView):
    model = Resource
    template_name = 'content/resource/resource_delete.html'
    success_url = ('resource_list')

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Resource, pk=pk)