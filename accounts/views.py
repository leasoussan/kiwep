from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings 
from django.core.mail import send_mail 
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic import View
from django.urls import reverse
from .forms import (
    MyUserCreationForm,
    MyUserChangeForm,
    StudentProfileCreationForm, 
    SpeakerProfileCreationForm, 
    RepresentativeProfileCreationForm,
)

from.models import Student, Speaker, Representative
from django.urls import reverse_lazy






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

def get_user_profile_form(request, user):
  
    if user.usertype == 'student':
        profile_form = StudentProfileCreationForm()
        return profile_form

    elif user.usertype  == 'speaker':  
        profile_form =SpeakerProfileCreationForm()
        return profile_form
         

    elif user.usertype == 'institution':
        profile_form =  RepresentativeProfileCreationForm()
        return profile_form


# -----------------------------------------------------------------------------------------------


class CreateProfile(View):
    def get(self, request , id):
        if id == 'student':
            profile_form = StudentProfileCreationForm()

        elif id  == 'speaker':  
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

            return redirect('{usertype}_dashboard')

        return render(request, 'accounts/profile/edit_profile.html', {'usertype':id.title(), 'form': profile_form})






class EditStudentProfile(View):
    def post(self, request, id=None):
        user_form = MyUserChangeForm(request.POST, id = request.user)
     
        profile_form = StudentProfileCreationForm(request.POST, id=request.user)
    
        
        if user_form.is_valid(self):
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = request.user
            profile.save()
            
            return redirect('{usertype}_dashboard')

        return ('profile')



def edit_profile(request, id):
    if request.method == "POST":
        user_form = MyUserChangeForm()
        if id == 'student':
            profile_form = StudentProfileCreationForm(request.POST, id=request.user)
    
        elif id == 'speaker':  
            profile_form = SpeakerProfileCreationForm(request.POST, id=request.user)

        elif id == 'institution':
            profile_form = RepresentativeProfileCreationForm(request.POST, id=request.user)


        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit = False)
            profile.user = request.user 
            profile.save()
            return redirect('profile_page')
    else:
        user_form = MyUserChangeForm(id=request.user)
        profile_form = get_user_profile_form(id=request.user.profile)
        args = {}
        # args.update(csrf(request))
        args['form'] = user_form
        args['profile_form'] = profile_form
        return render(request, 'artists/edit_profile.html', args)

