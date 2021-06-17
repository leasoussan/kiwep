from django.urls import path
from .views import (
    # my_inbox,
    DiscussionCreateView,
    DiscussionView,

)


urlpatterns = [
    # path('my_inbox', my_inbox, name= 'my_inbox'),
    path('discussion-add', DiscussionCreateView.as_view(), name= 'discussion_add'),
    path('discussion-view/<int:pk>', DiscussionView.as_view(), name= 'discussion_view'),
#   path('',.as_view(), name = '')
]
