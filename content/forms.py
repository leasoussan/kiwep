from django.forms import ModelForm 
from .models import Project


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

