from django.urls import path
from .views import (
    dashboard, 
    my_calendar_view,
    team_board,
    # CreateInstitutionProfile,
)



urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('calendar/', my_calendar_view, name='my_calendar'),
    path('team_board/', team_board, name='team_board'),
    # path('create-institution-profile/', CreateInstitutionProfile.as_view(), name='create_institution_profile'),

]
