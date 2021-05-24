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
            'is_template',
        ] 

        # exclude = ['completed', 'created_by']

class TeamAddForm(ModelForm):

    class Meta:
        model = Team
        fields = [
            'name',
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
    pass



mission_fields = (
        'name',
        'response_type',
        'stage',
        'field',
        'level',
        'description',
        'resources',
        'points',
        'acquired_skill',
        'due_date',
    )



class IndividualMissionAddForm(ModelForm):
    class Meta:
        model = IndividualMission
        fields = mission_fields



class CollectiveMissionAddForm(ModelForm):
    class Meta:
        model = CollectiveMission
        fields = mission_fields


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



CollectiveMissionFormSet = inlineformset_factory(
    Project,
    CollectiveMission,
    fields=mission_fields,
    extra=1)

IndividualMissionFormSet = inlineformset_factory(
    Project,
    IndividualMission,
    fields=mission_fields,
         extra=1)





class SubmitMissionForm(ModelForm):
    class Meta:
        model = IndividualCollectiveMission
        fields = [
            'response_comment',
            'response_file',
        ]