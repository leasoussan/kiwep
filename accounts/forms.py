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
    USER_TYPE = [
        ('is_student', _('student')),
        ('is_speaker', _('speaker')),
        ('is_representative', _('representative')),
    ]
    usertype = forms.ChoiceField(choices=USER_TYPE, label='Who are you?')
    email = forms.EmailField(max_length=60, help_text='Required. Add a valid email address')
    class Meta:
        model = MyUser
        fields = ['username', 'email', 'password1', 'password2', 'language_code']

          # labels ={
        #     'language_code': 'Language'
        # }


    # TODO: future further validation or others
    # def __init__(self, *args, **kwargs):
    #     """
    #       specifying styles to fields
    #     """
    #     super(MyUserCreationForm, self).__init__(*args, **kwargs)
    #     for field in (
    #     self.fields['email'], self.fields['username'], self.fields['password1'], self.fields['password2']):
    #         field.widget.attrs.update({'class': 'form-control '})
    #



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
        fields = ['user']
