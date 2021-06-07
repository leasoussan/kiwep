from django.urls import path
from .views import (
    my_inbox,
    CommentsTeamCreateView,
    CommentsTeamListView,

)


urlpatterns = [
    path('my_inbox', my_inbox, name= 'my_inbox') ,
    path('team-comments-add', CommentsTeamCreateView.as_view(), name= 'create_comments_team'),
    path('team-comments-list', CommentsTeamListView.as_view(), name= 'team_comments_list')
]
