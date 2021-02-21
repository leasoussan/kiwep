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
            user = authenticate(username= form.cleaned_data['username'], password =form.cleaned_data['password1'], usertype=form.cleaned_data['usertype'] )
            
            if user is not None:
                if user.get_user_type == 'Student':
                    login(request, user)
                    return redirect('student_create_profile')
            
                elif user.get_user_type == 'Speaker':  
                    login(request, user)  
                    return redirect('speaker_create_profile')

                elif user.get_user_type == 'Institution':
                    login(request, user)
                    return redirect('representative_create_profile')   



            return render(request, 'registration/register.html', {"form":form})      


# -----------------------------------------------------------------------------------------------

# ____________________________________________________________________________________________________CREATE PROFILE 


class StudentCreateProfile(CreateView):

    model = Student
    template_name = 'accounts/profile/edit_student_profile.html'
    form_class = StudentProfileCreationForm
    success_url = reverse_lazy('student_profile')

    def get_initial(self):
        initial = super().get_initial()
        return initial

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)








# _________________________________________________________________________________________________Speaker___CREATE PROFILE 


class SpeakerCreateProfile(CreateView):

    model = Speaker
    template_name = 'accounts/profile/edit_speaker_profile.html'
    form_class = SpeakerProfileCreationForm
    success_url = reverse_lazy('speaker_profile')

    def get_initial(self):
        initial = super().get_initial()
        return initial

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class InstitutionCreateProfile(CreateView):
    model = Representative
    template_name = 'profile/profile/edit_institution_profile.html'

    form_class = RepresentativeProfileCreationForm
    
    success_url = reverse_lazy('institution_profile')

    def get_initial(self):
        initial = super().get_initial()
        return initial

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    










# -----------------------------------------------------------------------------------------------INSTITUTION _registration

class RepresentativeCreateProfile(CreateView):
   pass



# _________________________________________________________________________________________________Institution___CREATE PROFILE 




# def institution_profile(request, pk):
#     institution = Institution.objects.get(pk=pk)
#     context={
#         'profile':profile,
#         'items':items
#     }

#     return render(request, 'artists/artist_profile.html', context)




