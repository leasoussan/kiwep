from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

from django.contrib.auth.decorators import user_passes_test, login_required
from django.urls import reverse_lazy

from accounts.decorators import check_profile
from accounts.mixin import StudentStatuPassesTestMixin
from .models import Comment, Discussion, Answer
from message.forms import AddDiscussionForm, AddCommentForm, AddAnswerForm, MissionSpeakerStatusAnswerForm, \
    MissionSpeakerGradeAnswerForm, StudentEditAnswerFrom
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


class GenericCustomRedirectView(RedirectView):

    pattern_name = 'comment_add'
    form_class = None

    def save_form(self, form):
        return form.save()

    def can_save(self,form):
        return True


    def get_redirect_url(self, *args, **kwargs):
        form = self.form_class(self.request.POST, self.request.FILES or None)
        fail = True
        if form.is_valid():
            if self.can_save(form):
                self.object = self.save_form(form)
                fail=False
                messages.success(self.request,  f'Your {self.object._meta.model.__name__} was added succesfuly')

        if fail:
            messages.warning(self.request, f'Your {self.object._meta.model.__name__} wasn\'t saved')

        return self.request.GET.get('next')




class RequestUserSaveFormMixin():

    def save_form(self, form):
        object = form.save(commit=False)
        object.user = self.request.user
        object.save()
        return object



class DiscussionCreateView(RequestUserSaveFormMixin, GenericCustomRedirectView):

    pattern_name = 'discussion_add'
    form_class = AddDiscussionForm



# ________________________________________________________________________________________Comment CreateView>>>>>>>>>>



class CommentCreateView(RequestUserSaveFormMixin, GenericCustomRedirectView):

    pattern_name = 'comment_add'
    form_class= AddCommentForm





class AnswerCreateView(StudentStatuPassesTestMixin, GenericCustomRedirectView):
    pattern_name = "create_answer"
    form_class = AddAnswerForm


    def can_save(self, form):
        mission = form.cleaned_data['content_type'].model_class().objects.get(id=form.cleaned_data['object_id'])
        if mission.__class__.__name__ == 'IndividualCollectiveMission':
            if self.request.user.profile() in mission.parent_mission.attributed_to.all():
                return True
        if mission.mission_type == 'i':
            if self.request.user == mission.attributed_to.user:
                return True
        if mission.mission_type == 'c':
            if self.request.user.profile() in mission.attributed_to.all():
                return True
        return False



class AnswerUpdateView(StudentStatuPassesTestMixin, UpdateView):
    model = Answer
    template_name = 'crud/update.html'
    fields = ['response_comment', 'response_file', ]

    def get_object(self):
        pk = self.kwargs.get("pk")
        return get_object_or_404(Answer, pk=pk)

    def get_success_url(self):
        return reverse_lazy('my_mission_list')

    def form_valid(self, form):
        return super().form_valid(form)


class AnswerDeletView(StudentStatuPassesTestMixin, DeleteView):
    model = Answer
    template_name = 'crud/delete.html'
    success_url = reverse_lazy('my_mission_list')

    def get_object(self, queryset=None):
        pk =self.kwargs['pk']
        return get_object_or_404(Answer, pk=pk)


class SpeakerAnswerMissionStatusView(UpdateView):
    model = Answer
    template_name = 'crud/update.html'
    success_url = reverse_lazy('dashboard')
    form_class = MissionSpeakerStatusAnswerForm


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)

    def get_success_url(self):
        return reverse_lazy('team_list')

    def form_valid(self, form):
        print(f'form errors {form.errors}')
        return super().form_valid(form)


class SpeakerGradeAnswerView(UpdateView):
    model =Answer
    template_name = "crud/update.html"
    success_url = reverse_lazy()
    form_class = MissionSpeakerGradeAnswerForm


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)


    def get_success_url(self):
        return reverse_lazy('team_list')


    def form_valid(self, form):
        return super().form_valid(form)


















