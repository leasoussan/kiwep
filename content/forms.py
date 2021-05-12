from django import forms
from django.forms import ModelForm 
from .models import Project, Team, Mission, Resource, CollectiveMission, IndividualMission, IndividualCollectiveMission
from accounts.models import Student
from django.forms import inlineformset_factory
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.db.models import Q

class ProjectAddForm(ModelForm):
    class Meta:
        model = Project
        fields = [
            'name',
            'description',
            'time_to_complete',
            'field',
            'difficulty',
            'points',

        ] 

        # exclude = ['completed', 'created_by']

class TeamAddForm(ModelForm):
    """def__init__: Is to say that we are calling the for super() with it's packed data
    then we go into the project fields, qnd change the quesry set to filter our Q request and dispose it to us"""

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['project'].queryset = Project.objects.filter(Q(is_template=True) | Q(speaker=user.profile()))


    class Meta:
        model = Team
        fields = [
            'name',
            'project',
            'start_date',
            'due_date',
            'group_Institution',
            'participants',
        ]

    
class AddMemberTeamForm(ModelForm):
    """ Speaker can add team memebers"""
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
            'points',
            'response_type',
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
  

CollectiveMissionFormSet = inlineformset_factory(
    Project,
    CollectiveMission,
    fields=(
        'attributed_to', 
        'due_date', 
        'stage',
       
        ),
         extra=0,

    widgets = {
            'attributed_to': FilteredSelectMultiple(verbose_name='Team Participants', is_stacked=False)
        }
)

IndividualMissionFormSet = inlineformset_factory(
    Project,
    IndividualMission,
    fields=(
        'attributed_to', 
        'due_date', 
        'stage',
       
        ),
         extra=0)





class SubmitMissionForm(ModelForm):
    class Meta:
        model = IndividualCollectiveMission
        fields = [
            'response_comment',
            'response_file',
        ]