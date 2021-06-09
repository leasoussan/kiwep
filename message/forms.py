from django import forms
from django.forms import ModelForm
from .models import Comment, Discussion



class AddCommentsTeamForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = '__all__'

    # comment_text = forms.CharField(max_length=200, widget=forms.TextInput(attrs={"rows": 5, "cols": 20}))
#





