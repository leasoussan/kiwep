from django.urls import path
from django.contrib.auth import views as auth_views
from accounts.views import (
    school_dashboard, 
    register, 
    StudentSignUp, 
    SpeakerSignUp, 
    InstitutionSignUp,
    StudentCreateProfile,
    SpeakerCreateProfile,
    InstitutionCreateProfile,
    InstitutionProfile,
)

urlpatterns = [
    path('school_dashboard/', school_dashboard, name='school_dashboard'),
    path('register/', register, name='register'),
    path('student_register/', StudentSignUp.as_view(), name="student_register"),
    path('speaker_register/', SpeakerSignUp.as_view(), name="speaker_register"),
    path('institution_register/', InstitutionSignUp.as_view(), name="institution_register"),


    # profile creat, edit and view 
    path('student_create_profile/', StudentCreateProfile.as_view(), name="student_create_profile"),
    path('speaker_create_profile/', SpeakerCreateProfile.as_view(), name="speaker_create_profile"),
    path('institution_create_profile/', InstitutionCreateProfile.as_view(), name="institution_create_profile"),
    path('institution_profile/<int:pk>', InstitutionProfile.as_view(), name="institution_profile"),

   
]
