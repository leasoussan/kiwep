from django.urls import path
from .views import (
    speaker_dashboard, 
)



urlpatterns = [
    path('speaker-dashboard/<int:id>', speaker_dashboard, name='speaker_dashboard'),
]
