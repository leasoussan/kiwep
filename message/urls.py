from django.urls import path
from .views import (
    # my_inbox,
    DiscussionCreateView,
    CommentCreateView,

)


urlpatterns = [
    # path('my_inbox', my_inbox, name= 'my_inbox'),
    path('discussion-add', DiscussionCreateView.as_view(), name= 'discussion_add'),
    path('comment-add/',CommentCreateView.as_view(), name = 'comment_add')
]
