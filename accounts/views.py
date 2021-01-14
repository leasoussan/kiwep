from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.conf import settings 
from django.core.mail import send_mail 

from django.urls import reverse
from .forms import CustomUserCreationForm


def school_dashboard(request):
    return render(request, "accounts/school_dashboard.html")



def register(request):
    if request.method == "GET":
        return render(request, 'registration/register.html', {"form": CustomUserCreationForm})

    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse('school_dashboard'))