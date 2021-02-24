from django.urls import path
from django.contrib.auth import views as auth_views
from accounts.views import (
     
    Register, 
    CreateProfile,
    # EditProfile,
    ProfileView,
    # profile,
    edit_profile,

    
 )

urlpatterns = [
    
    path('register/', Register.as_view(), name='register'),
    path('create-profile/<str:id>/', CreateProfile.as_view(), name='create_profile'),
    path('edit-profile/<int:id>', edit_profile, name="edit_profile"),
    path('profile/<int:id>', ProfileView.as_view(), name="profile"),
    # path('profile/', profile, name="profile"),
    # path('edit-profile/<int:id>', EditProfile.as_view(), name="edit_profile"),
    
    # path('student_create_profile/', EditStudentProfile.as_view(), name="student_edit_profile"),
    # path('speaker_create_profile/', SpeakerCreateProfile.as_view(), name="speaker_create_profile"),
    # path('institution_create_profile/', RepresentativeCreateProfile.as_view(), name="representative_create_profile"),
    # path('institution_profile/<int:pk>', InstitutionProfile.as_view(), name="institution_profile"),

   
]
