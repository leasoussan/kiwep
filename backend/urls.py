from django.urls import path
from .views import (
    dashboard, 
    my_calendar_view,
)



urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('calendar/', my_calendar_view, name='my_calendar'),


]
