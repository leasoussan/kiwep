from .models import Student, Speaker, Representative
from django.shortcuts import redirect
from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth.decorators import user_passes_test, login_required


def check_profile(user, return_tuple= False):
    ''' Check if profile exists Boolean'''
    exists = True
    if user.is_student and not Student.objects.filter(user=user).exists():
        exists = False
        p_type = 'is_student'

    if user.is_speaker and not Speaker.objects.filter(user=user).exists():   
        exists =  False
        p_type = 'is_speaker'

    if user.is_representative and not Representative.objects.filter(user=user).exists():
        exists = False
        p_type = 'is_representative'

    if return_tuple:
        return exists, p_type

    return exists






def login_check(user):
    if user.is_authenticated:
        return redirect('homepage.html') 
    else:
        return redirect('login.html')



# def missing_profile_type(user):
#     ''' Function to check which profile is missing '''
#     if user.is_student and not Student.objects.filter(user=user).exists():
#         return 'is_student'

#     if user.is_speaker and not Speaker.objects.filter(user=user).exists():   
#         return 'is_speaker'

#     if user.is_representative and not Representative.objects.filter(user=user).exists():
#         return 'is_represnetative'


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




def student_check(user):
    # print(user.get_user_type())
    return user.get_user_type() == "student"



