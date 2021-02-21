from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings 
from django.core.mail import send_mail 
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic import View
from django.urls import reverse
from .forms import (
    MyUserCreationForm,
    StudentProfileCreationForm, 
    SpeakerProfileCreationForm, 
    RepresentativeProfileCreationForm,
)

from.models import Student, Speaker, Representative
from django.urls import reverse_lazy




def school_dashboard(request):
    return render(request, "accounts/school_dashboard.html")


# -----------------------------------------------------------------------------------Resistration and Profile Creation


class Register(View):
    def get(self, request):
        context = {
         "form": MyUserCreationForm()

        }
        return render(request, 'registration/register.html', context)

    def post(self, request):
        form = MyUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save() 
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            usertype=form.cleaned_data['usertype'] 
            user = authenticate(username= username, password = password, usertype =usertype)
            login(request, user)

            
            
            return redirect('create_profile', form.cleaned_data['usertype'])


        return render(request, 'registration/register.html', {"form":form})      


# -----------------------------------------------------------------------------------------------

class CreateProfile(View):
    def get(self, request,id=None):
        if id == 'student':
            profile_form = StudentProfileCreationForm()
    
        elif id == 'speaker':  
            profile_form = SpeakerProfileCreationForm()

        elif id == 'institution':
            profile_form = RepresentativeProfileCreationForm()

        return render(request, 'accounts/profile/edit_profile.html', {'usertype':id.title(), 'form': profile_form})
        

    def post(self, request,  id=None):
        if id == 'student':
            profile_form = StudentProfileCreationForm(request.POST)
    
        elif id == 'speaker':  
            profile_form = SpeakerProfileCreationForm(request.POST)

        elif id == 'institution':
            profile_form = RepresentativeProfileCreationForm(request.POST)

        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.user = request.user
            profile.save()

            return redirect('homepage')

        return render(request, 'accounts/profile/edit_profile.html', {'usertype':id.title(), 'form': profile_form})
 