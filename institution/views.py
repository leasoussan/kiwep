from django.shortcuts import render
from django.contrib.auth import get_user_model


User = get_user_model()
# Create your views here.


def institution_homepage(request):
    return render(request, 'institution/institution_home_page.html')