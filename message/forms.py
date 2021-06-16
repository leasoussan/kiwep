from django import forms
from django.forms import ModelForm
from .models import Comment, Discussion



class AddDiscussionForm(forms.ModelForm):

    class Meta:
        model = Discussion
        # exclude = ['user']
        fields = ['title', 'comment_text', 'content_type', 'object_id']
        widgets={
            'content_type':forms.HiddenInput(),
            'object_id': forms.HiddenInput()
        }





