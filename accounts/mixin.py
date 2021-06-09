from django.shortcuts import render, reverse
from django.contrib.auth.views import redirect_to_login
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from accounts.decorators import check_profile, speaker_check
from django.http import Http404


class ProfileCheckPassesTestMixin(UserPassesTestMixin):

    '''The ProfileCheck is to see if User created a profile after registration
     test_func : get a boolean True or False'''
    
    def test_func(self):
        return check_profile(self.request.user)
    
    
    def get_login_url(self):
        if not self.request.user.is_authenticated:
            return super().get_login_url()
        else:

            return reverse('create_profile')

    def handle_no_permission(self):
        return redirect_to_login(self.request.get_full_path(), self.get_login_url(), self.get_redirect_field_name())








class SpeakerStatuPassesTestMixin(UserPassesTestMixin):
    """ Checking if the user is a Speaker"""

    def test_func(self):
       return speaker_check(self.request.user) and check_profile(self.request.user)
    
    
    def get_login_url(self):
        if not self.request.user.is_authenticated:
            return super().get_login_url()

    def handle_no_permission(self):
        return redirect_to_login(self.request.get_full_path(), self.get_login_url(), self.get_redirect_field_name())








class StudentStatuPassesTestMixin(UserPassesTestMixin):
    """ Checking if the user is a Speaker"""

    def test_func(self):
        return student_check(self.request.user) and check_profile(self.request.user)

    def get_login_url(self):
        if not self.request.user.is_authenticated:
            return super().get_login_url()


    def handle_no_permission(self):
        return redirect_to_login(self.request.get_full_path(), self.get_login_url(), self.get_redirect_field_name())

















class RepresentativeStatuPassesTestMixin(UserPassesTestMixin):
    """ Checking if the user is a Speaker"""

    def test_func(self):
        return representative_check(self.request.user) and check_profile(self.request.user)

    def get_login_url(self):
        if not self.request.user.is_authenticated:
            return super().get_login_url()

    def handle_no_permission(self):
        return redirect_to_login(self.request.get_full_path(), self.get_login_url(), self.get_redirect_field_name())





def speaker_check(user):

    return user.is_speaker



def student_check(user):

    return user.is_student



def representative_check(user):

    return user.is_representative