from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test, login_required
from accounts.decorators import check_profile

# Create your views here.

@login_required
@user_passes_test(check_profile, login_url='create_profile')
def my_inbox(request): 
    return render(request, 'message/my_inbox.html')