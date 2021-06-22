from django import forms
from django.forms import ModelForm
from .models import Comment, Discussion, Answer


class AddDiscussionForm(forms.ModelForm):

    class Meta:
        model = Discussion
        # exclude = ['user']
        fields = ['title', 'comment_text', 'content_type', 'object_id']
        widgets={
            'content_type':forms.HiddenInput(),
            'object_id': forms.HiddenInput()
        }





class AddCommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        # exclude = ['user']
        fields = ['comment_text', 'content_type', 'object_id']
        widgets={
            'content_type':forms.HiddenInput(),
            'object_id': forms.HiddenInput()
        }




class AddAnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['response_comment','response_file', 'content_type', 'object_id']
        widgets = {
            'content_type': forms.HiddenInput(),
            'object_id': forms.HiddenInput()
        }


class MissionSpeakerStatusAnswerForm(forms.ModelForm):

    class Meta:
        model = Answer
        fields = ['status']

        widgets = {
            'content_type': forms.HiddenInput(),
            'object_id': forms.HiddenInput(),
            'status': forms.Select(attrs={'onchange':'this.form.submit()'})
        }

