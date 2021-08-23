from django import forms
from django.forms import ModelForm
from .models import Comment, Discussion, Answer


class AddDiscussionForm(forms.ModelForm):

    class Meta:
        model = Discussion
        # exclude = ['user']
        fields = ['title', 'comment_text', 'content_type', 'object_id']
        widgets={
            'comment_text': forms.Textarea(attrs={'rows': 2, 'cols': 5}),
            'content_type':forms.HiddenInput(),
            'object_id': forms.HiddenInput()
        }





class AddCommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['comment_text', 'content_type', 'object_id']

        widgets={
            'comment_text':forms.Textarea(attrs={'rows': 2, 'cols': 8}),
            'content_type':forms.HiddenInput(),
            'object_id': forms.HiddenInput()
        }



class AddAnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['response_comment','response_file', 'content_type', 'object_id']
        widgets = {
            'response_comment':forms.Textarea(attrs={'rows': 2, 'cols':5}),
            'content_type': forms.HiddenInput(),
            'object_id': forms.HiddenInput(),
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

class MissionSpeakerGradeAnswerForm(forms.ModelForm):

    class Meta:
        model = Answer
        fields = ['grade']

        widgets = {
            'content_type': forms.HiddenInput(),
            'object_id': forms.HiddenInput(),
            'status': forms.Select(attrs={'onchange':'this.form.submit()'})
        }
