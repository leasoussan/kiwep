import django.forms.widgets
from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.forms import ModelForm
from django.forms import inlineformset_factory

from django.http import Http404
from django.utils.translation import ugettext as _
from accounts.models import Student
from backend.models import Field
from .models import Project, Team, Resource, Mission, CollectiveMission, IndividualMission, IndividualCollectiveMission


class ProjectAddForm(ModelForm):
    class Meta:
        model = Project
        fields = [
            'name',
            'description',
            'time_to_complete',
            'points',
            'is_template'
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
    #
    start_date = forms.DateField(
        widget=django.forms.DateInput(
            format='%d/%m/%Y',
            attrs={'type': 'date'}),
    )




class AddMemberTeamForm(ModelForm):
    """ Speaker can add team memebers"""
    class Meta:
        model = Team
        fields = ['participants']

        widgets = {
            'participants': FilteredSelectMultiple(verbose_name='participants_list', is_stacked=False)
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




class UpdateTeamForm(ModelForm):
    class Meta:
        model = Team
        fields = [
            'name',
            'project',
            'start_date',
            'participants',
            'project_completed' ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['project'].queryset = kwargs['instance'].manager.project_set.available_projects()
        if kwargs['instance'].project:
            self.fields['project'].queryset |= Project.objects.filter(id=kwargs['instance'].project.id)

class ProjectTeamAddForm(ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'start_date', 'participants']




mission_fields = [
    'stage',
    'response_type',
    'name',
    'description',
    'points',
    'acquired_skill',
    'due_date',
]


class IndividualMissionAddForm(ModelForm):
    class Meta:
        model = IndividualMission
        fields = mission_fields + ['attributed_to']

# TODO: Check date setup
# # Check if a date is not in the past.
#         if data < datetime.date.today():
#             raise ValidationError(_('Invalid date - renewal in past'))
#
#         # Check if a date is in the allowed range (+4 weeks from today).
#         if data > datetime.date.today() + datetime.timedelta(weeks=4):
#             raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))
#
#         # Remember to always return the cleaned data.
#         return data

class CollectiveMissionAddForm(ModelForm):
    class Meta:
        model = CollectiveMission
        fields = mission_fields + ['attributed_to']





class BulkAddMissionForm(forms.Form):
    # MISSION_TYPE=[
    #     ('i', _('individual_mission')),
    #     ('c', _('collective_mission')),
    # ]
    projects=forms.ModelMultipleChoiceField(queryset=Project.objects.all(), widget=forms.CheckboxSelectMultiple)
    # mission_type = forms.Select(choices=MISSION_TYPE)

    def __init__(self, projects=None, *args, **kwargs):
        super(BulkAddMissionForm, self).__init__(*args, **kwargs)
        if projects:
            self.fields['projects'].queryset = projects

    # def save_bulk_mission(self, mission):
    #     print('valid')
    #     for project in self.cleaned_data['projects']:
    #         mission = project.mission
    #         mission.id=None


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
    link= forms.URLField(initial='http://', required=False)




#
# CollectiveMissionFormSet = inlineformset_factory(
#     Project,
#     CollectiveMission,
#     fields=mission_fields,
#     extra=1)
#
# IndividualMissionFormSet = inlineformset_factory(
#     Project,
#     IndividualMission,
#     fields=mission_fields,
#     extra=1)
#



# {TODO}
class addSkillsForm(forms.Form):
    field = Field.objects.all()
    name = forms.CharField(max_length=20)


    def save_add_skill(self):

        object.acquired_skills = self.cleaned_data['name']









# ____________________________________________________________________________Validate Mission----------------------
class ValidateMissionForm(forms.Form):
    accepted = forms.BooleanField()


    def validate_mission(self, mission):
        mission = IndividualMission.objects.get(id= mission.id)
        mission.accepted = True
        mission.save()



