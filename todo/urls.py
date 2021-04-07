from django.urls import path
from . import api_views, views

urlpatterns = [
    path('', api_views.todoOverview, name='my_tasks'),
    path('task_list/', api_views.taskList, name='task_list'),
    path('task_detail/<int:pk>/', api_views.taskDetail, name='task_detail'),
    path('task_create/', api_views.task_create, name='task_create'),
    path('task_update/<int:pk>/', api_views.task_update, name='task_update'),
    path('task_delete/<int:pk>', api_views.task_delete, name='task_delete'),

    # front_end
    path('frontend_list_view/', api_views.frontend_list_view, name='frontend_list'),
   


# todo backend

    path('add-personal-task/', views.PersonalTaskCreateView.as_view(), name = 'add_personal_task'),
    path('add-team-task/', views.TeamTaskCreateView.as_view(), name = 'add_team_task'),
    path('todo_list/', views.MyTasksView.as_view(), name='todo_list'),
    path('task-detail/<int:pk>', views.PersonalTaskDetailView.as_view() , name = 'task_detail'),
    path('team_task_detail/<int:pk>', views.TeamTaskDetailView.as_view() , name = 'team_task_detail')
]


