from django.urls import path
from . import api_views

urlpatterns = [
    path('', api_views.todoOverview, name='my_tasks'),
    path('task_list/', api_views.taskList, name='task_list'),
    path('task_detail/<int:pk>/', api_views.taskDetail, name='task_detail'),
    path('task_create/', api_views.task_create, name='task_create'),
    path('task_update/<int:pk>/', api_views.task_update, name='task_update'),
    path('task_delete/<int:pk>', api_views.task_delete, name='task_delete'),

    # front_end
    path('frontend_list_view/', api_views.frontend_list_view, name='frontend_list'),
   

]

