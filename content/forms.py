from django import forms
from django.http import Http404
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

    start_date = forms.DateField(
        widget=forms.DateInput(format='%d/%m/%Y'),
        input_formats=('%d-%m-%Y',)
    )

    due_date = forms.DateField(
        widget=forms.DateInput(format='%d/%m/%Y'),
        input_formats=('%d-%m-%Y',)
    )

    # def clean(self):
    #     cleaned_data = super().clean()
    #     start_date = cleaned_data.get("start_date")
    #     end_date = cleaned_data.get("end_date")
    #     if end_date < start_date:
    #         raise forms.ValidationError("End date should be greater than start date.")
    #
    #     return self.cleaned_data
    
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





class CollectiveMissionAssign(forms.Form):

    participants = forms.ModelMultipleChoiceField(queryset=Student.objects.all())

    def __init__(self, **kwargs):
        team = kwargs['team']
        if not team.project:
            raise Http404("You dont Have a Projects")

        super().__init__()
        self.fields['participants'].queryset = team.participants.all()




    def save(self, collective_mission):
        # if self.is_valid():
            for participant in self.cleaned_data['participants']:
                mission= IndividualCollectiveMission.objects.get_or_create(parent_mission=collective_mission,  attributed_to = participant )
                
                












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