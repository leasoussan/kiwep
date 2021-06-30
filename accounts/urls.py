from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, LogoutView
from accounts.views import page_404

from accounts.views import (
    MyLoginView,
    Register,
    CreateProfile,
    EditProfile,
    MyProfileView,
    ProfileView,
    InstitutionInviteView,


)

urlpatterns = [

    path('register/', Register.as_view(), name='register'),
    path('login/', MyLoginView.as_view() ,name='login'),

    path('create-profile/', CreateProfile.as_view(), name='create_profile'),
    path('profile/<int:id>',MyProfileView.as_view(), name="profile"),
    path('edit-profile/', EditProfile.as_view(), name="edit_profile"),
    path('profile_view/<int:pk>', ProfileView.as_view(), name = "profile_view"),
    path('institution-invite/<str:key>', InstitutionInviteView.as_view(), name = "institution_invite"),
]





