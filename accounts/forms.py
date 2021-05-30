
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.conf import settings
from django import forms
from django.db import transaction 
from .models import Student, Speaker, Representative, MyUser

from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _

User = get_user_model()




# Form to create a basic User 
class MyUserCreationForm(UserCreationForm):
    USER_TYPE=[
        ('is_student',_('student')),
        ('is_speaker', _('speaker')),
        ('is_representative', _('representative')), 
    ]
    usertype = forms.ChoiceField(choices=USER_TYPE, label = 'Who are you?')
    

    class Meta:
        model = MyUser
        fields = ['username', 'email', 'password1', 'password2', 'language_code']


        # labels ={
        #     'language_code': 'Language'
        # }



class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Email / Username')





class UserForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = [
            'first_name', 
            'last_name',
            'phone_number',
            'profile_pic', 
            'city']
























# Form To create Profile 

class StudentProfileCreationForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ['user', 'softs_skills'] 



class SpeakerProfileCreationForm(forms.ModelForm):
    class Meta:
        model = Speaker
        exclude = ['user'] 


class RepresentativeProfileCreationForm(forms.ModelForm):
    class Meta:
        model = Representative
        exclude = ['user'] 
    



