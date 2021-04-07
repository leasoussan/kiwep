from django.forms import ModelForm
from django.forms import inlineformset_factory
from django.contrib.admin.widgets import FilteredSelectMultiple
from .models import Task, PersonalTask

class AddPersonalTaskForm(ModelForm):
    class Meta:
        model = PersonalTask
        fields = '__all__'