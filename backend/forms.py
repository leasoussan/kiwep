from django.forms import ModelForm 
from .models import Institution

class InstitutionAddForm(ModelForm):
    model = Institution
    exclude = ['user']

    

