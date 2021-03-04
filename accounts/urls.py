from django.urls import path
from django.contrib.auth import views as auth_views
from accounts.views import (  
    Register, 
    CreateProfile,
    EditProfile,
    MyProfileView,
    # my_profile
    
    

 )

urlpatterns = [
    
    path('register/', Register.as_view(), name='register'),
    path('create-profile/<str:id>/', CreateProfile.as_view(), name='create_profile'),
    path('profile/<int:id>',MyProfileView.as_view(), name="profile"),
    path('edit-profile/', EditProfile.as_view(), name="edit_profile"),
    
   
]
