from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

from django.contrib.auth.decorators import user_passes_test, login_required
from accounts.decorators import check_profile
from .models import Comment, Discussion
from message.forms import AddDiscussionForm, AddCommentForm
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



# ________________________________________________________________________________________Comment CreateView>>>>>>>>>>




class CommentCreateView(RedirectView):

    pattern_name = 'comment_add'

    def get_redirect_url(self, *args, **kwargs):
        form = AddCommentForm(self.request.POST)


        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = self.request.user
            comment.save()


            messages.success(self.request,  'Your Comment was added succesfuly')

        else:
            messages.warning(self.request, 'Your Comment wasn\'t saved')

        return self.request.GET.get('next')







