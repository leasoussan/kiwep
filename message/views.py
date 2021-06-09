from django.shortcuts import render

from django.contrib.auth.decorators import user_passes_test, login_required
from accounts.decorators import check_profile
from .models import Comment, Discussion
from message.forms import AddCommentsTeamForm
from django.views.generic import (
    CreateView, 
    DetailView, 
    ListView, 
    DetailView, 
    UpdateView, 
    DeleteView
)

# Create your views here.

@login_required
@user_passes_test(check_profile, login_url='create_profile')
def my_inbox(request): 
    return render(request, 'message/my_inbox.html')



class CommentsTeamCreateView(CreateView):
    model = Comment
    template = 'comments/comments_team.html'
    form = AddCommentsTeamForm


    def form_valid(self, form):
        pass



class CommentsTeamListView(ListView):
    model = Comment
    template_name = 'comments/comments_team.html'

    context_object_name = 'team_comments'


    def get_queryset(self):
        return self.request.user.commentsteam_set.all()

   
class CommentMissionDeleteView():

    pass


class CommentMissionUpdate():
    pass