from django.shortcuts import render, get_object_or_404
from django.views.generic import (
   View
)


def homepage_view(request):
    return render(request, 'homepage.html')