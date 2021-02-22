from django.shortcuts import render
from django.contrib.auth import get_user_model

# Create your views here.
User = get_user_model()


def speaker_dashboard(request, id):
    user = User.objects.get(id = id)
    context = {
        'user': user,
       
         
    }
    

    return render(request, "accounts/speaker_dashboard.html", {'queryset': user})
