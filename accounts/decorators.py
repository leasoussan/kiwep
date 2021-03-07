from .models import Student, Speaker, Representative
from django.shortcuts import redirect

from django.http import HttpResponse


def check_profile(user):
    if user.get_user_type == 'student':
        user = Student.objects.filter(user=user).exists()

    elif user.get_user_type == 'speaker':  
        user =  Speaker.objects.filter(user=user).exists()

    
    elif user.get_user_type == 'representative':
        user =  Representative.objects.filter(user=user).exists()

    return user



# def login_check(user):
#     if user.is_authenticated:
#         return redirect('homepage.html') 
#     else:
#         return redirect('login.html')