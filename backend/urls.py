from django.urls import path
from .views import (
    dashboard,
InstitutionAddGroupView,


)



urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),

    path('add_group/', InstitutionAddGroupView.as_view(), name='add_group'),

]
