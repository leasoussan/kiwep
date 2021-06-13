from django.shortcuts import render, get_object_or_404
from django.views.generic import (
   View
)
from .forms import TeamAddForm



def homepage_view(request):
    return render(request, 'homepage.html')

# def date_message(request):
#     context = {}
#     form = TeamAddForm(request.POST or None)
#     context['form'] = form
#     if request.POST:
#         if form.is_valid():
#             temp = form.cleaned_data.get("start_date")
#             print(temp)
#     return render(request, "create_team_mission.html", context)
