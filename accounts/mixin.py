from django.shortcuts import render, reverse
from django.contrib.auth.views import redirect_to_login
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from accounts.decorators import check_profile, speaker_check
from django.http import Http404


class ProfileCheckPassesTestMixin(UserPassesTestMixin):
    '''test_furn : get a boolean True or False'''
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
    
    def test_func(self):
       return speaker_check(self.request.user) and check_profile(self.request.user)
    
    
    def get_login_url(self):
        if not self.request.user.is_authenticated:
            return super().get_login_url()
        else:
            raise Http404
    
    def handle_no_permission(self):
        return redirect_to_login(self.request.get_full_path(), self.get_login_url(), self.get_redirect_field_name())
