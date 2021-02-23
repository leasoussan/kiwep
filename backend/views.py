from django.shortcuts import render
from django.contrib.auth import get_user_model

# Create your views here.
User = get_user_model()


def dashboard(request):
    

    return render(request, "backend/general_dashboard.html")
