from django.shortcuts import render, redirect,get_object_or_404
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

from.models import Student, Speaker, Representative, User
from django.urls import reverse_lazy


# ----------------------------------------------------------------------------------Mixin

# class ProfileCheckUserPassesTestMixin(UserPassesTestMixin):
#     def test_func(self):
#         return check_profile(self.request.user)
    
    
#     def get_login_url(self):
#         if not self.request.user.is_authenticated:
#             return super().get_login_url()
#         else:
#             return '/create_profile/'

#     def handle_no_permission(self):
#         return redirect_to_login(self.request.get_full_path(), self.get_login_url(), self.get_redirect_field_name())





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


def get_user_profile_form(request, usertype): 
    
    data = request.POST or None 

    if  usertype == 'student':
        profile_form = StudentProfileCreationForm(data)
       

    elif usertype  == 'speaker':  
        profile_form =SpeakerProfileCreationForm(data)
    

    elif usertype == 'representative':
        profile_form =  RepresentativeProfileCreationForm(data)
    
    return profile_form


# -----------------------------------------------------------------------------------------------


class CreateProfile(View):
    def get(self, request , id):
        profile_form = get_user_profile_form(request, id)
        return render(request, 'accounts/profile/edit_profile.html', {'usertype':id.title(), 'form': profile_form})
        

    def post(self, request,  id=None):
        
        profile_form = get_user_profile_form(request, id)

        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.user = request.user
            profile.save()

            return redirect('dashboard')

        return render(request, 'accounts/profile/edit_profile.html', {'usertype':id.title(), 'form': profile_form})



# -----------------------------------------------------------Profile


class ProfileView(View):

    def get(self, request, id):
        user = User.objects.get(id=id)
        profile = user.profile
        return render(request, 'accounts/profile/profile.html', {'usertype':user, 'form': profile})


# def profile(request):
#     return render(request, 'accounts/profile/profile.html')



# ----------------------------------------------------------------------------

    
class EditProfile(UpdateView): 
    model = User 
   
    template_name = 'accounts/profile/profile.html'

    def get(self, request , id):
        user_form = MyUserChangeForm(request.user)
        profile_form_edit = get_user_profile_form(request, id)
        return render(request, 'accounts/profile/edit_profile.html', {'user':user_form, 'form': profile_form_edit})
        

    def post(self, request,  id=None):
        user = User.objects.get(id=id)
        profile_form_edit = get_user_profile_form(request, id)

        if profile_form_edit.is_valid():
            profile = profile_form_edit.save(commit=False)
            profile.user = request.user
            profile.save()

            return redirect(f'profile')

        return render(request, 'accounts/profile/edit_profile.html', {'user':user, 'form': profile_form_edit})



    
def edit_profile(request, id=None):
    usertype = request.user.get_user_type
    if request.method == 'POST':
        user_form = MyUserChangeForm(request.POST,request.FILES,instance=request.user)
        edit_profile = get_user_profile_form(request, usertype)  

        if user_form.is_valid() and edit_profile.is_valid():
            user = user_form.save()
            updated_form = edit_profile.save(False)
            updated_form.user = user
            updated_form.save()
            return redirect('profile')
        
    else:
        user_form = MyUserChangeForm(instance=request.user)
        edit_profile = get_user_profile_form(request, usertype)  
 
        args = {
            'user_form': user_form,
            'edit_profile' : edit_profile
        }
      
        return render(request, 'accounts/edit_profile.html', args)


