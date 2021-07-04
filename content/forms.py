import django.forms.widgets
from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.forms import ModelForm
from django.forms import inlineformset_factory
from django.http import Http404

from accounts.models import Student
from .models import Project, Team, Resource, CollectiveMission, IndividualMission, IndividualCollectiveMission


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
            'group_Institution',
            'participants',
        ]

    start_date = forms.DateField(
        widget=django.forms.DateInput(
            format='%d/%m/%Y',
            attrs={'type': 'date'}),
        # input_formats=('%d-%m-%Y',),
    )


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
    


mission_fields = [
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
]



class IndividualMissionAddForm(ModelForm):
    class Meta:
        model = IndividualMission
        fields = mission_fields

    due_date = forms.DateField(
        widget=django.forms.DateInput(
            format='%d/%m/%Y',
            attrs={'type': 'date'}),
        # input_formats=('%d-%m-%Y',),
    # resources = forms.ModelMultipleChoiceField(queryset=object.team_set.project.resources.all)
    )


class CollectiveMissionAddForm(ModelForm):
    class Meta:
        model = CollectiveMission
        fields = mission_fields

    due_date = forms.DateField(
        widget=django.forms.DateInput(
            format='%d/%m/%Y',
            attrs={'type': 'date'}),
        # input_formats=('%d-%m-%Y',),
    )


class CollectiveMissionAssign(forms.Form):
    participants = forms.ModelMultipleChoiceField(queryset=Student.objects.all())


    def save_individuals(self, collective_mission):
        print('is valid')
        for participant in self.cleaned_data['participants']:
            mission= IndividualCollectiveMission.objects.get_or_create(
                                                        parent_mission=collective_mission,
                                                        attributed_to = participant)

            print('participant', participant)






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

    link= forms.URLField(initial='http://')





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




# ____________________________________________________________________________Validate Mission----------------------
class ValidateMissionForm(forms.Form):
    accepted = forms.BooleanField()


    def validate_mission(self, mission):
        mission = IndividualMission.objects.get(id= mission.id)
        mission.accepted = True
        mission.save()



