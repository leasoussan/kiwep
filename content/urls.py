from django.urls import path
from content.views import * 

urlpatterns = [
    path('project_list/', ProjectListView.as_view(), name = "project_list"),
    path('project_detail/<int:pk>', ProjectDetailView.as_view(), name = "project_detail"),
    path('create_project/', ProjectCreatelView.as_view(), name = "create_project"),
]
