from .models import Student, Speaker, Representative
from django.shortcuts import redirect
from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth.decorators import user_passes_test, login_required


def check_profile(user):
    exists = False
    if user.get_user_type() == 'student':
        exists = Student.objects.filter(user=user).exists()

    elif user.get_user_type() == 'speaker':  
        exists =  Speaker.objects.filter(user=user).exists()

    
    elif user.get_user_type() == 'representative':
        exists =  Representative.objects.filter(user=user).exists()

    return exists

# we need a True or false answer to be able if user passes test 



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


def speaker_check(user):
    # print(user.get_user_type())
    return user.get_user_type() == "speaker"

