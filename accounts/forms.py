
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.conf import settings
from django import forms
from django.db import transaction 
from .models import Student, Speaker, Representative

from django.contrib.auth import get_user_model


User = get_user_model()



# Form to create a basic User 
class MyUserCreationForm(UserCreationForm):
    USER_TYPE=[
        ('student','student'),
        ('speaker', 'speaker'),
        ('representative', 'representative'), 
    ]
    usertype = forms.ChoiceField(choices=USER_TYPE)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    

    # def clean_username(self):
    #     username = self.cleaned_data.get('username')
    #     queryset = User.objects.get(username__iexact=username)
    #     if not queryset.exists():
    #         raise forms.ValidationError("Invalid name")
    #     return username
        


    





class UserForm(forms.ModelForm):
    class Meta:
        model = User
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
        exclude = ['user'] 



class SpeakerProfileCreationForm(forms.ModelForm):
    class Meta:
        model = Speaker
        exclude = ['user'] 


class RepresentativeProfileCreationForm(forms.ModelForm):
    class Meta:
        model = Representative
        exclude = ['user'] 




