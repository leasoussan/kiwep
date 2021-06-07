from django import forms
from django.forms import ModelForm
from .models import CommentsTeam



class AddCommentsTeamForm(forms.ModelForm):

    class Meta:
        model = CommentsTeam
        fields = ['comment_text']

    comment_text = forms.CharField(max_length=200, widget=forms.TextInput(attrs={"rows": 5, "cols": 20}))
#