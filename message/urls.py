from django.urls import path
from .views import (
    # my_inbox,
    DiscussionCreateView,

    CommentCreateView,
    AnswerCreateView,
    SpeakerAnswerMissionStatusView
)


urlpatterns = [
    # path('my_inbox', my_inbox, name= 'my_inbox'),
    path('discussion-add', DiscussionCreateView.as_view(), name= 'discussion_add'),

    path('comment-add/',CommentCreateView.as_view(), name = 'comment_add'),
    path('answer-add/', AnswerCreateView.as_view(), name='answer_add'),
    path('answer-edit-status/<int:pk>', SpeakerAnswerMissionStatusView.as_view(), name='answer_edit_status'),
    #   path('',.as_view(), name = '')

]
