from django.forms import ModelForm 
from .models import Project, Team


class ProjectAddForm(ModelForm):
    class Meta:
        model = Project
        fields = [
            'name',
            'description',
            'time_to_complet',
            'field',
            'difficulty',
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
            'participants',
            'tasks',
            'final_project',
        ] 
        