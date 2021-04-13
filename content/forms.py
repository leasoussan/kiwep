from django import forms
from django.forms import ModelForm 
from .models import Project, Team, Mission, Resource, TeamProjectMission
from accounts.models import Student
from django.forms import inlineformset_factory
from django.contrib.admin.widgets import FilteredSelectMultiple

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
            'participants'
        ] 
    
class AddMemberTeamForm(ModelForm):
    class Meta:
        model = Team
        fields = ['participants'] 
        
        widgets = {
            'participants': FilteredSelectMultiple(verbose_name='Participants List', is_stacked=False)
        }

        # class media is built inside django 

    class Media:
            css = {
                'all': ('/static/admin/css/widgets.css',),
            }
            js = ('/admin/jsi18n',)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['participants'].queryset = kwargs['instance'].group_Institution.student_set.all()


    





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


# ProjectMissionFormSet = inlineformset_factory(
#     Project, Mission,
#     fields ='__all__' )
  

TeamProjectMissionFormSet = inlineformset_factory(
    Team, 
    TeamProjectMission, 
    fields=(
        'attributed_to', 
        'due_date', 
        'is_collective',
        'is_collective_individual'
        ),
         extra=0)

    


class SubmitMissionForm(ModelForm):
    class Meta:
        model = TeamProjectMission
        fields = [
            'response_text',
            'response_file',
        ]