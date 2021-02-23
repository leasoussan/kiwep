from django.shortcuts import render, get_object_or_404
from .models import Mission
from django.forms import ModelForm
from .forms import MissionAddForm
from django.urls import reverse_lazy


from django.views.generic import (
    CreateView, 
    DetailView, 
    ListView, 
    DetailView, 
    UpdateView, 
    DeleteView
)


class MissionListView(ListView):
    model = Mission
    template_name = 'content/mission/mission_list.html'    
    context_object_name = 'mission_list'






class MissionDetailView(DetailView):
    model = Mission
    template_name = 'content/mission/mission_detail.html'    
    

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Mission, pk=pk)




class MissionCreateView(CreateView):
    model = Mission
    form_class = MissionAddForm 
    template_name = 'content/mission/mission_create.html'  
    
    def form_valid(self, form):
        self.object = form.save()

        return super().form_valid(form)



class MissionUpdateView(UpdateView):
    model = Mission
    fileds = ['name', 
            'field', 
            'level',
            'description',
            'completed',
            'resources',]
    template_name = 'content/mission/mission_create.html'  


class MissionDeleteView(DeleteView):
    model = Mission
    template_name = 'content/mission/mission_delete.html' 
    success_url = reverse_lazy('mission-list')