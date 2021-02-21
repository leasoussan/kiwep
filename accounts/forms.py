
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.conf import settings
from django import forms
from django.db import transaction 
from .models import Student, Speaker, Representative

from django.contrib.auth import get_user_model






# Form to create a basic User 
class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2', 'usertype')
    

    # get_usertype 
    def get_user_type(self):
        return self.usertype



# Form To change Basic Info- name -user or password 
class MyUserChangeForm(UserChangeForm):

    class Meta:
        model = get_user_model()
        fields = ('username', 'first_name', 'last_name', 'email')




# Form To create Profile 

class StudentProfileCreationForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = '__all__'



class SpeakerProfileCreationForm(forms.ModelForm):
    class Meta:
        model = Speaker
        exclude = ['user'] 


class RepresentativeProfileCreationForm(forms.ModelForm):
    class Meta:
        model = Representative
        exclude = ['user'] 






