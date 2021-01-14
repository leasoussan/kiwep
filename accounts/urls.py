from django.urls import path, include
from django.contrib.auth import views as auth_views
from accounts.views import school_dashboard, register

urlpatterns = [
    path('school_dashboard/', school_dashboard, name='school_dashboard'),
    path('register/', register, name="register"),

]
