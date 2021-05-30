from django.shortcuts import render, redirect,get_object_or_404, reverse
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
    UserForm,
    StudentProfileCreationForm, 
    SpeakerProfileCreationForm, 
    RepresentativeProfileCreationForm,
    UserForm,
 
)
from django.urls import reverse_lazy
from django.contrib.auth.views import redirect_to_login
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from accounts.mixin import ProfileCheckPassesTestMixin
from django.contrib.auth.decorators import user_passes_test, login_required
from .mailer import *
from.models import Student, Speaker, Representative, MyUser
from accounts.decorators import check_profile, login_check
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages

# ----------------------------------------------------------------------------------Mixin





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
            
            setattr(user, usertype, True)
            
            user.save()
            user = authenticate(username= username, password = password, usertype =usertype)
            login(request, user)
            send_welcome_signup(user)
            
            return redirect(reverse('create_profile'), form.cleaned_data['usertype'])


        return render(request, 'registration/register.html', {"form":form})      






# -----------------------------------------------------------------------------------------------


def get_user_profile_form(request, usertype, edit=False): 
    """ This function allows is to check which profile is requested, 
    and to know what page/authorization to direct it to"""
    
    if edit: 
        instance = request.user.profile() 
    else: 
        instance = None


    data = request.POST or None 
    print(usertype)
    if  usertype == 'student':
        profile_form = StudentProfileCreationForm(data, instance=instance )
    

    elif usertype  == 'speaker':
        profile_form =SpeakerProfileCreationForm(data, instance=instance)
    

    elif usertype == 'representative':
        profile_form =  RepresentativeProfileCreationForm(data, instance=instance)
    
    return profile_form




class CreateProfile(View):
    """ Any one who creats an accounts will be directed to create a Profile, 
    and wont be able to do any actions unless this is done"""
    
    def get(self, request ):
        user_form = UserForm(instance = request.user)
        usertype = check_profile(request.user, True)[1]
        profile_form = get_user_profile_form(request, usertype)
        
        return render(request, 'accounts/profile/edit_profile.html', {'usertype':usertype, 'profile_form': profile_form, 'user_form': user_form})
       

    def post(self, request):
        user_form = UserForm(request.POST, instance = request.user)
        usertype = check_profile(request.user, True)[1]
        profile_form = get_user_profile_form(request, usertype)
        valuenext= request.POST.get('next')

        if profile_form.is_valid() and user_form.is_valid():
            user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = request.user

            profile.save()

            return redirect('dashboard')

        # messages.add_message(request, messages.ERROR, 'You have an error in your form')

        return render(request, 'accounts/profile/edit_profile.html', {'usertype':usertype, 'form': profile_form})





# -----------------------------------------------------------------------------------------------



# -----------------------------------------------------------Profile


class MyProfileView(ProfileCheckPassesTestMixin, View):
    """ This view is to show the User Profile view"""
    def get(self, request, id):
        user = MyUser.objects.get(id=id)
        profile_view = user.profile
        return render(request, 'accounts/profile/profile.html', {'user':user, 'profile_view': profile_view})






# ----------------------------------------------------------------------------

    
class EditProfile(ProfileCheckPassesTestMixin, View): 
    """ Edit Profile """
    def get(self, request):
        user_form = UserForm(instance =request.user)
        profile_form = get_user_profile_form(request, request.user.get_user_type(), edit =True) 
        
        return render(request, 'accounts/profile/edit_profile.html', {'user_form':user_form, 'profile_form': profile_form})
        

    def post(self, request):
        user_form = UserForm(request.POST, instance = request.user)
        profile_form = get_user_profile_form(request, request.user.get_user_type(), edit =True) 
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile',request.user.id)

        return render(request, 'accounts/profile/edit_profile.html', {'user_form':user_form, 'profile_form': profile_form})






class MyLoginView(LoginView):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('homepage')
        return super().get(self, request, *args, **kwargs)


class ProfileView(View):
    """ View to show profile view - not logged in User"""
    'profile_view'
    pass



def page_404(request):
    """ 404 Page Not Found"""
    return render(request, '404.html')