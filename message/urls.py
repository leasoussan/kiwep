from django.urls import path
from .views import (
    # my_inbox,
    DiscussionCreateView,

)


urlpatterns = [
    # path('my_inbox', my_inbox, name= 'my_inbox'),
    path('discussion-add', DiscussionCreateView.as_view(), name= 'discussion_add'),
#   path('', .as_view(), name= '')
#   path('',.as_view(), name = '')
]
