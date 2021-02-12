



from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings 
from django.core.mail import send_mail 
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic import View
from django.urls import reverse
from .forms import StudentCreationForm, SpeakerCreationForm, InstitutionCreationForm, InstitutionProfileCreateForm

from.models import Institution
from django.urls import reverse_lazy




def school_dashboard(request):
    return render(request, "accounts/school_dashboard.html")


# -----------------------------------------------------------------------------------Resistration and Profile Creation


def register(request):
    return render(request, "registration/register.html")


# -----------------------------------------------------------------------------------------------STUDENT Registration


class StudentSignUp(CreateView):
    def get(self, request):
        context = {
         "form": StudentCreationForm()

        }
        return render(request, 'registration/student_registration.html', context)

    def post(self, request):
        form = StudentCreationForm(request.POST)
       
        if form.is_valid():
            user = form.save() 
            user = authenticate(username= form.cleaned_data['username'], password =form.cleaned_data['password1'])
            
            if user is not None:
                login(request, user)
                # send_welcome_signup(user)
                # this is ref to mailer 
            
                return redirect('create_profile_student')
        return render(request, 'registration/student_registration.html', {"form":form})      




# ____________________________________________________________________________________________________CREATE PROFILE 
class StudentCreateProfile(CreateView):

    pass






# -----------------------------------------------------------------------------------------------SPEAKER Register
class SpeakerSignUp(CreateView):
    def get(self, request):
        context = {
         "form": SpeakerCreationForm()

        }
        return render(request, 'registration/speaker_registration.html', context)

    def post(self, request):
        form = SpeakerCreationForm(request.POST)
   
        if form.is_valid():
            user = form.save() 
            user = authenticate(username= form.cleaned_data['username'], password =form.cleaned_data['password1'])
            
            if user is not None:
                login(request, user)
                # send_welcome_signup(user)
                # this is ref to mailer 
            
                return redirect('create_profile_speaker')
        return render(request, 'registration/signuspeaker_registrationp.html', {"form":form})      


# _________________________________________________________________________________________________Speaker___CREATE PROFILE 

class SpeakerCreateProfile(CreateView):
    model = Institution
    template_name = 'profile/edit_institution_profile.html'

    form_class = InstitutionCreationForm
    success_url = reverse_lazy('institution_profile')











# -----------------------------------------------------------------------------------------------INSTITUTION _registration

class InstitutionSignUp(CreateView):
    def get(self, request):
        context = {
         "form": InstitutionCreationForm()

        }
        return render(request, 'registration/institution_registration.html', context)

    def post(self, request):
        form = InstitutionCreationForm(request.POST)
      
        if form.is_valid():
            user = form.save() 
            user = authenticate(username= form.cleaned_data['username'], password =form.cleaned_data['password1'])
            
            if user is not None:
                login(request, user)
                # send_welcome_signup(user)
                # this is ref to mailer 
            
                return redirect('institution_create_profile')
        return render(request, 'registration/institution_registration.html', {"form":form})      




# _________________________________________________________________________________________________Institution___CREATE PROFILE 

class InstitutionCreateProfile(CreateView):

    model = Institution
    template_name = 'registration/profile/edit_institution_profile.html'
    form_class = InstitutionProfileCreateForm
    success_url = reverse_lazy('institution_profile')

    
    

    def get_initial(self):
        initial = super().get_initial()
        return initial


    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    





class InstitutionProfile(DetailView):
    model = Institution
 




# def institution_profile(request, pk):
#     institution = Institution.objects.get(pk=pk)
#     context={
#         'profile':profile,
#         'items':items
#     }

#     return render(request, 'artists/artist_profile.html', context)




