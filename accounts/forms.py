
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from django import forms
from django.db import transaction 
from .models import Student, Speaker, Institution

from django.contrib.auth import get_user_model


User = get_user_model()


# class MyUserCreationForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', ]


class MyUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email',)









class StudentCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', ]



class SpeakerCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', ]


class InstitutionCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', ]



class InstitutionProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Institution 
        exclude = ['user'] 



class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('username', 'email')

