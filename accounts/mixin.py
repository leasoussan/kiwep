from django.contrib.auth.views import redirect_to_login
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from accounts.decorators import check_profile


class ProfileCheckPassesTestMixin(UserPassesTestMixin):
    def test_func(self):
        return check_profile(self.request.user)
    
    
    def get_login_url(self):
        if not self.request.user.is_authenticated:
            return super().get_login_url()
        else:
            return 'create_profile/'

    def handle_no_permission(self):
        return redirect_to_login(self.request.get_full_path(), self.get_login_url(), self.get_redirect_field_name())

