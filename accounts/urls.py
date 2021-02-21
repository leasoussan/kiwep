from django.urls import path
from django.contrib.auth import views as auth_views
from accounts.views import (
    school_dashboard, 
    Register, 
    CreateProfile,
    
 )

urlpatterns = [
    path('school_dashboard/', school_dashboard, name='school_dashboard'),
    path('register/', Register.as_view(), name='register'),
    path('create_profile/<str:id>/', CreateProfile.as_view(), name='create_profile'),
   


    # profile creat, edit and view 
    # path('student_create_profile/', StudentCreateProfile.as_view(), name="student_create_profile"),
    # path('speaker_create_profile/', SpeakerCreateProfile.as_view(), name="speaker_create_profile"),
    # path('institution_create_profile/', RepresentativeCreateProfile.as_view(), name="representative_create_profile"),
    # path('institution_profile/<int:pk>', InstitutionProfile.as_view(), name="institution_profile"),

   
]
