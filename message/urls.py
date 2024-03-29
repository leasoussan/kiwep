from django.urls import path
from .views import (
    # my_inbox,
    DiscussionCreateView,
    AnswerDeletView,
    CommentCreateView,
    AnswerCreateView,
    SpeakerAnswerMissionStatusView,
    SpeakerGradeAnswerView, AnswerUpdateView,
)


urlpatterns = [
    # path('my_inbox', my_inbox, name= 'my_inbox'),
    path('discussion-add/', DiscussionCreateView.as_view(), name= 'discussion_add'),

    path('comment-add/',CommentCreateView.as_view(), name = 'comment_add'),
    path('answer-add/', AnswerCreateView.as_view(), name='create_answer'),
    path('answer-edit/<int:pk>', AnswerUpdateView.as_view(), name='update_answer'),
    path('delete-edit/<int:pk>', AnswerDeletView.as_view(), name='delete_answer'),
    path('answer-edit-status/<int:pk>', SpeakerAnswerMissionStatusView.as_view(), name='answer_edit_status'),
    path('answer-grade/<int:pk>', SpeakerGradeAnswerView.as_view(), name='answer_grade_add'),

    #   path('',.as_view(), name = '')

]
