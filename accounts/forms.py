from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.conf import settings
from django import forms
from django.db import transaction
from .models import Student, Speaker, Representative, MyUser, InstitutionInvite, SpeakerInvite

from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _
# SET UP THE FORMS
# form django.core.urlresolvers import reverse
# from crispy_forms.bootstrap import Field, InlineRadios, TabHolder, Tab
# from crispy_forms.helper import FormHelper
#
# from crispy_forms.layout import Submit, Layout, Div, Fieldset
# # END setting Form

import django.forms.widgets

User = get_user_model()


# Form to create a basic User
class MyUserCreationForm(UserCreationForm):
    USER_TYPE = [
        ('is_student', _('student')),
        ('is_speaker', _('speaker')),
    ]
    usertype = forms.ChoiceField(choices=USER_TYPE, label='Who are you?')
    email = forms.EmailField(max_length=60, help_text='Required. Add a valid email address')
    class Meta:
        model = MyUser
        fields = ['username', 'email', 'password1', 'password2', 'language_code']




    # labels ={
        #     'language_code': 'Language'
        # }





class MySpeakerCreationForm(MyUserCreationForm):
    
    usertype = forms.CharField(label='Who are you?', initial ='is_speaker', widget=forms.HiddenInput())




class InstitutionCreationForm(UserCreationForm):
    usertype = forms.CharField(label='Who are you?', widget=forms.HiddenInput())
    email = forms.EmailField(max_length=60, help_text='Required. Add a valid email address')
    fields = forms
    class Meta:
        model = MyUser
        fields = ['username', 'email', 'password1', 'password2', 'language_code']



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

    # def clean(self):
    #     super(UserForm, self).clean()
    #     first_name = self.cleaned_data.get('first_name')
    #     last_name = self.cleaned_data.get('first_name')
    #     profile_pic = self.cleaned_data.get('profile_pic')
    #     phone_number =self.cleaned_data.get('phone_number')
    #     if not first_name:
    #         raise forms.ValidationError(_('please_enter_first_nsame'), code='invalid')
    #
    #     if not last_name:
    #         raise forms.ValidationError(_('please_enter_last_nsame'), code='invalid')
    #
    #     # if phone_number < len(10) or phone_number > len(10):
    #     #     raise forms.ValidationError(_('invalid_number_message'), code='invalid')
    #     # if profile_pic:
    #     #     if profile_pic._height > 1920 or profile_pic._width > 1080:
    #     #         raise forms.ValidationError("Height or Width is larger than what is allowed")
    #     return self.cleaned_data

# Form To create Profile

class StudentProfileCreationForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ['user', 'softs_skills', 'class_level']

    dob = forms.DateField(
        widget=django.forms.DateInput(
            format='%d/%m/%Y',
            attrs={'type': 'date'}),
    )

    join_code = forms.CharField(max_length=10, required=False)
    
    def __init__(self, *args, **kwargs):

        if 'instance' in kwargs:
            if kwargs['instance'] == None:
                super(StudentProfileCreationForm, self).__init__(*args, **kwargs)
            else:
                kwargs['initial'] = {'join_code':kwargs['instance'].class_level.join_code}
        super(StudentProfileCreationForm, self).__init__(*args, **kwargs)

        "To have it disabled when editing "
        if 'instance' in kwargs:
            if kwargs['instance'] != None:
                self.fields['join_code'].disabled = True


        
        
class SpeakerProfileCreationForm(forms.ModelForm):
    class Meta:
        model = Speaker
        exclude = ['user', 'institution']


#
# class RepresentativeProfileCreationForm(forms.ModelForm):
#     class Meta:
#         model = Representative
#         fields = ['user']
#
#
#
#
# class InstitutionInviteForm(forms.ModelForm):
#
#     class Meta:
#         model = InstitutionInvite
#         fields = ['email']




class SpeakerInviteForm(forms.ModelForm):
    class Meta:
        model = SpeakerInvite
        fields = ['email']