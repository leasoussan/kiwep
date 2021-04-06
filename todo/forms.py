from django import forms
from django.forms import inlineformset_factory
from django.contrib.admin.widgets import FilteredSelectMultiple
from .models import Task, PersonalTask

class AddPersonalTaskForm(forms.ModelForm):
    model = PersonalTask
    fields = [
        '__all__'
    ]