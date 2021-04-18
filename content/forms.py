from django import forms
from django.forms import ModelForm 
from .models import Project, Team, Mission, Resource, CollectiveProjectMission, IndividualProjectMission
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
            'missions'
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
  

CollectiveProjectMissionFormSet = inlineformset_factory(
    Team, 
    CollectiveProjectMission, 
    fields=(
        'attributed_to', 
        'due_date', 
        'stage',
       
        ),
         extra=0)

    


IndividualProjectMissionFormSet = inlineformset_factory(
    Team, 
    IndividualProjectMission, 
    fields=(
        'attributed_to', 
        'due_date', 
        'stage',
       
        ),
         extra=0)


# TeamCollectiveMissionFormSet = inlineformset_factory(
#     Team, 
#     TeamCollectiveMission
 
#     fields=(
#         'attributed_to', 
#         'due_date', 
#         'stage',
       
#         ),
#          extra=0)


class SubmitMissionForm(ModelForm):
    class Meta:
        model = IndividualProjectMission
        fields = [
            'response_comment',
            'response_file',
        ]