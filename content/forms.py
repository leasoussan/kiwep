from django import forms
from django.forms import ModelForm 
from .models import Project, Team, Mission, Resource
from accounts.models import Student

class ProjectAddForm(ModelForm):
    class Meta:
        model = Project
        fields = [
            'name',
            'description',
            'time_to_complet',
            'field',
            'difficulty',
        ] 

        # exclude = ['completed', 'created_by']

class TeamAddForm(ModelForm):
    class Meta:
        model = Team
        fields = [
            'name',
            'project',
            'start_date',
            'due_date',
            'group_Institution',
            'participants',
            'final_project',
        ] 
        
        participants = forms.ModelMultipleChoiceField(
        queryset=Student.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    



class MissionAddForm(ModelForm):
    class Meta:
        model = Mission

        fields = [
            'name', 
            'field', 
            'level',
            'description',
            'resources',
            'points'
            
        ]


class ResourceAddForm(ModelForm):
    class Meta:
        model = Resource

        fields = [
            'name', 
            'link',
            'text',
            'field',
            'image',
            'file_rsc',
        ]