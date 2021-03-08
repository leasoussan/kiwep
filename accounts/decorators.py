from .models import Student, Speaker, Representative
from django.shortcuts import redirect
from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth.decorators import user_passes_test, login_required


def check_profile(user):
    if user.get_user_type == 'student':
        user = Student.objects.filter(user=user).exists()

    elif user.get_user_type == 'speaker':  
        user =  Speaker.objects.filter(user=user).exists()

    
    elif user.get_user_type == 'representative':
        user =  Representative.objects.filter(user=user).exists()

    return user



def login_check(user):
    if user.is_authenticated:
        return redirect('homepage.html') 
    else:
        return redirect('login.html')



# to have a page that is you are login id not needed to use the decorators
# def logout_required(function=None, logout_url=settings.LOGOUT_URL):
#     actual_decorator = user_passes_test(
#         lambda u: not u.is_authenticated,
#         login_url=logout_url
#     )
#     if function:
#         return actual_decorator(function)
#     return actual_decorator