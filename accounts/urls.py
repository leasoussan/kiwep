from django.urls import path
from django.contrib.auth import views as auth_views
from accounts.views import (
     
    Register, 
    CreateProfile,
    # EditProfile,
    profile_view,
    edit_profile,
    EditStudentProfile
    
 )

urlpatterns = [
    
    path('register/', Register.as_view(), name='register'),
    path('create-profile/<str:id>/', CreateProfile.as_view(), name='create_profile'),
    path('edit-profile/<int:pk>', edit_profile, name="edit_profile"),
    path('student-edit-profile/<int:pk>/', EditStudentProfile.as_view(), name="student_create_profile"),
    path('profile/', profile_view, name="profile"),
    
    # path('student_create_profile/', EditStudentProfile.as_view(), name="student_edit_profile"),
    # path('speaker_create_profile/', SpeakerCreateProfile.as_view(), name="speaker_create_profile"),
    # path('institution_create_profile/', RepresentativeCreateProfile.as_view(), name="representative_create_profile"),
    # path('institution_profile/<int:pk>', InstitutionProfile.as_view(), name="institution_profile"),

   
]
