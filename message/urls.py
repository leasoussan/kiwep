from django.urls import path
from .views import  (
    my_inbox,
)

urlpatterns = [
    path('my_inbox', my_inbox, name= 'my_inbox')   
]
