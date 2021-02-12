
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.conf import settings
from django import forms
from django.db import transaction 
from .models import Student, Speaker, Representative

from django.contrib.auth import get_user_model






# Form to create a basic User 
class MyUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email',)


# Form To change Basic Info- name -user or password 
class MyUserChangeForm(UserChangeForm):

    class Meta:
        model = settings.AUTH_USER_MODEL
        fields = ('username', 'email')




# Form To create Profile 

class StudentProfileCreationForm(UserCreationForm):
    class Meta:
        model = Student
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', ]



class SpeakerProfileCreationForm(UserCreationForm):
    class Meta:
        model = Speaker
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', ]


class RepresentativeCreationForm(UserCreationForm):
    class Meta:
        model = Representative
        fields = ['username', 'email', 'password1', 'password2', ]



class RepresentativeProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Representative 
        exclude = ['user'] 




