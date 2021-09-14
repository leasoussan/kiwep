from django.forms import ModelForm
from .models import Institution, Group
from django import forms

class InstitutionAddForm(ModelForm):
    class Meta:
        model = Institution
        exclude = ['representative']
        website = forms.URLField(initial='http://', required=False)




class InstitutionAddGroupForm(ModelForm):
    class Meta:
        model=Group
        exclude = ['institution']
