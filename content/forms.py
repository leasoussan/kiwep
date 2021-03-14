from django import forms
from django.forms import ModelForm 
from .models import Project, Team, Mission, Resource, TeamProjectMission
from accounts.models import Student
from django.forms import inlineformset_factory

class ProjectAddForm(ModelForm):
    class Meta:
        model = Project
        fields = [
            'name',
            'description',
            'time_to_complet',
            'field',
            'difficulty',
            'points',
            'mission'
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
            'final_project',
        ] 
    




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


# ProjectMissionFormSet = inlineformset_factory(Project, MissionsProject, fields ='__all__' )

TeamProjectMissionFormSet = inlineformset_factory(Team, TeamProjectMission, exclude=('team', 'created_date', 'completed' , 'attributed_to'),  extra=1)


