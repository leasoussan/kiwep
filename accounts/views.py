from django.shortcuts import render, redirect,get_object_or_404, reverse
from django.contrib.auth import views as auth_views
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from django.core.mail import send_mail
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic import View, RedirectView
from django.urls import reverse

from backend.models import Institution
from .forms import (
    MyUserCreationForm,
    UserForm,
    StudentProfileCreationForm,
    SpeakerProfileCreationForm,
    UserForm,
    LoginForm, InstitutionInviteForm, MySpeakerCreationForm, InstitutionCreationForm
)
from backend.forms import InstitutionAddForm

from django.urls import reverse_lazy
from django.contrib.auth.views import redirect_to_login
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from accounts.mixin import ProfileCheckPassesTestMixin, SpeakerStatuPassesTestMixin, RepresentativeStatuPassesTestMixin
from django.contrib.auth.decorators import user_passes_test, login_required
from .mailer import *
from .models import Student, Speaker, Representative, MyUser, InstitutionInvite, random_token, SpeakerInvite
from accounts.decorators import check_profile, login_check
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from datetime import datetime, timedelta, date
from django.utils.translation  import ugettext as _
# ----------------------------------------------------------------------------------Mixin





# -----------------------------------------------------------------------------------Resistration and Profile Creation



class Register(View):
    def get(self, request):
        form = MyUserCreationForm()

        if 'key' in  request.GET:
            form = MySpeakerCreationForm(initial={'usertype': 'is_speaker'})

        context = {
         "form": form
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

            if user.is_speaker:
                key = request.GET.get('key')
                if SpeakerInvite.objects.filter(key=key, used=False).exists():
                    invite = SpeakerInvite.objects.get(key=key)
                    invite.used = True
                    user.save()
                    invite.joined_user = user
                    invite.save()

            user.save()
            user = authenticate(username= username, password = password, usertype =usertype)
            login(request, user)
            send_welcome_signup(user)


            return redirect(reverse('create_profile'), form.cleaned_data['usertype'])

        return render(request, 'registration/register.html', {"form":form})






# -----------------------------------------------------------------------------------------------


def is_key_valid(request, key, use= False):
    thirty_days = date.today() - timedelta(days=30)

    if InstitutionInvite.objects.filter(key=key).exists():
        invite = InstitutionInvite.objects.get(key=key)
        if invite.used:
            messages.error(request, _("invite_used"))
            return False

        elif invite.date_invited < thirty_days:
            messages.error(request, _("your_invite_expired"))
            return False
    else:
        messages.error(request, _("no_key_to_register"))
        return False

    if use:
        invite.used=True
        invite.save()
    return True



class InstitutionInviteView(View):
    def get(self, request, **kwargs):
        key=self.kwargs['key']
        if not is_key_valid(request, key):
            return redirect('homepage')
        context = {
            "form": InstitutionCreationForm(initial={'usertype': 'is_representative'})
        }
        return render(request, 'registration/register.html', context)

    def post(self, request, **kwargs):
        key = self.kwargs['key']

        if not is_key_valid(request, key, use=True):
            return redirect('homepage')

        form = InstitutionCreationForm(request.POST)


        if form.is_valid():
            user = form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            usertype = form.cleaned_data['usertype']

            setattr(user, usertype, True)


            user.save()
            user = authenticate(username=username, password=password, usertype=usertype)
            login(request, user)
            send_welcome_signup(user)

            return redirect(reverse('create_profile'), form.cleaned_data['usertype'])

        return render(request, 'registration/register.html', {"form": form})


# -----------------------------------------------------------------------------------------------


def get_user_profile_form(request, edit=False):

    """ This function allows is to check which profile is requested, 
    and to know what page/authorization to direct it to"""
    user = request.user

    if edit:
        instance = user.profile()
    else: 
        instance = None

    data = request.POST or None 

    if user.is_student:

        profile_form = StudentProfileCreationForm(data, instance=instance )


    elif user.is_speaker:
        profile_form =SpeakerProfileCreationForm(data, instance=instance)


    elif user.is_representative:
        profile_form = InstitutionAddForm(data)

    return profile_form


# ------------------------------------------------------------------------------------------------------------


class CreateProfile(View):
    """ Any one who creats an accounts will be directed to create a Profile,
    and wont be able to do any actions unless this is done"""

    def get(self, request ):

        user_form = UserForm(instance =request.user)
        profile_form = get_user_profile_form(request)
        user = request.user
        if user.is_speaker:
            invites = user.received_invites.all()
            if invites.exists():
                institution= invites.first().institution
                profile_form.fields['group'].queryset = institution.group_set.all()

        return render(request, 'accounts/profile/edit_profile.html', {'profile_form': profile_form,
                                                                      'user_form': user_form,}
                      )


    def post(self, request):
        user_form = UserForm(request.POST,  request.FILES,  instance= request.user)
        profile_form = get_user_profile_form(request)
        user = request.user

        if profile_form.is_valid() and user_form.is_valid():

            user_form.save()
            object= profile_form.save(commit=False)

            if request.user.is_representative:
                object.representative = Representative.objects.get_or_create(user=request.user)[0]
            else:
                object.user = request.user
            object.save()
            if user.is_speaker:
                for invite in user.received_invites.all():
                    object.institution.add(invite.institution)
            return redirect('dashboard')



        # messages.add_message(request, messages.ERROR, 'You have an error in your form')

        return render(request, 'accounts/profile/edit_profile.html', {'user_form':user_form, 'form': profile_form, 'institution_form':institution_form})







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

        profile_form = get_user_profile_form(request, edit =True)
        

        return render(request, 'accounts/profile/edit_profile.html', {'user_form':user_form, 'profile_form': profile_form})


    def post(self, request):
        user_form = UserForm(request.POST, request.FILES, instance=request.user)
        print(user_form)
        profile_form = get_user_profile_form(request, edit =True)

        if user_form.is_valid() and profile_form.is_valid():
            print(user_form)
            user_form.save()
            profile_form.save()
            return redirect('profile',request.user.id)

        return render(request, 'accounts/profile/edit_profile.html', {'user_form':user_form, 'profile_form': profile_form})




# ------------------------------------------------------------------------------------------------------------
#
# class MyLoginView(LoginView):
#
#     def get(self, request, *args, **kwargs):
#         if request.user.is_authenticated:
#             return redirect('homepage')
#         return super().get(self, request, *args, **kwargs)


# ------------------------------------------------------------------------------------------------------------

#
#
# class MyLoginView(auth_views.LoginView):
#     form_class = LoginForm
#     template_name = 'registration/login.html'



class MyLoginView(LoginView):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')
        return super().get(self, request, *args, **kwargs)




def get_profile(request):
    if request.profile.is_student:
        return Student.objects.get(pk=pk)


    if request.profile.is_speaker:
        return Speaker.objects.get(pk=pk)

    if request.profile.is_institution:
        return Institution.objects.get(pk=pk)

    else:
        return "you dont have access here"



class ProfileView(DetailView):

    def get(self, request):
        """ View to show profile view - other logged in User"""
        return get_profile(request)





def page_404(request):
    """ 404 Page Not Found"""
    return render(request, '404.html')




#
# class InstitutionInviteView(View):
#     def get(self, request):
#         form = InstitutionInviteForm
#
#         return render(request, 'accounts/invite/invite.html', {'form': form})
#
#     def post(self, request):
#         if request.method == "POST":
#             form = InstitutionInviteForm(request.POST)
#             email= form.cleaned_data["email"]
#             print(form)
#             print(email)
#             if form.is_valid():
#                 institution_invite = form.save(commit=False)
#                 institution_invite.user = self.request.user
#                 institution_invite.key = random
#                 institution_invite = InstitutionInvite.object.get_or_create(request.user, email)
#
#                 institution_invite.send_institution_signup_invit(email)
#
#                 return redirect('institution_invite')
#
#             return redirect('institution_invite')
#
#

#
# class SpeakerInviteView(View):
#     def get(self, request):
#         form = SpeakerInviteForm
#
#         return render(request, 'accounts/invite/invite.html', {'form': form})
#
#     def post(self, request):
#         if request.method == "POST":
#             form = InstitutionInviteForm(request.POST)
#             email= form.cleaned_data["email"]
#             key = random_token()
#             print(form)
#             print(email)
#             if form.is_valid():
#                 speaker_invite = form.save(commit=False)
#
#                 user = self.request.user
#                 speaker_invite = InstitutionInvite.object.get_or_create(user=request.user, email=email, keay=key )
#
#                 speaker_invite.send_speaker_signup_invit(email)
#
#             return redirect('speaker_invite')
#
#         return redirect('speaker_invite')
#
