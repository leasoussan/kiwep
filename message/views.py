from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

from django.contrib.auth.decorators import user_passes_test, login_required
from accounts.decorators import check_profile
from .models import Comment, Discussion
from message.forms import AddDiscussionForm
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView, RedirectView
)

# Create your views here.

# @login_required
# @user_passes_test(check_profile, login_url='create_profile')
# def my_inbox(request):
#     return render(request, 'message/my_inbox.html')



class DiscussionCreateView(RedirectView):

    pattern_name = 'discussion_add'

    def get_redirect_url(self, *args, **kwargs):
        form = AddDiscussionForm(self.request.POST)
        if form.is_valid():
            discussion = form.save(commit=False)
            discussion.user = self.request.user
            discussion.save()

            messages.success(self.request,  'Your Discussion was added succesfuly')

        else:
            messages.warning(self.request, 'Your Discussion wasn\'t saved')

        return self.request.GET.get('next')




class DiscussionListView(ListView):
    model = Discussion
    context_object_name = "discussion_list"


    def get_queryset(self):
        return self.get_queryset().filter(title__id=self.object_id)




class DiscussionView(DetailView):
    model = Discussion
    template_name = 'comments/discussion.html'



#
# class CommentView(ListView):
#     model = Comment
#     template_name = 'comments/comments_team.html'
#
#     context_object_name = 'team_comments'
#
#
#     def get_queryset(self):
#         return self.request.user.commentsteam_set.all()

   
class CommentMissionDeleteView():

    pass


class CommentMissionUpdate():
    pass