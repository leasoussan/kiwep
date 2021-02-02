from django.urls import path
from . import views

urlpatterns = [
    path('', views.todoOverview, name='my_tasks'),
    path('task_list/', views.taskList, name='task_list'),
    path('task_detail/<int:pk>/', views.taskDetail, name='task_detail'),
    path('task_create/', views.task_create, name='task_create'),
    path('task_update/<int:pk>/', views.task_update, name='task_update'),
    path('task_delete/<int:pk>', views.task_delete, name='task_delete'),

    # front_end
    path('frontend_list_view/', views.frontend_list_view, name='frontend_list'),
   

]

