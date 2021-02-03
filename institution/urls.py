from django.urls import path
from . import views 

urlpatterns = [
    path('institution_homepage/', views.institution_homepage,  name = 'institution_home_page')
  
]
