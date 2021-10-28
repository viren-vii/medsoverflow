from django.db.models import fields
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'description', 'tags']
        widgets = {
          'title': forms.Textarea(attrs={'rows':1, 'cols':120}),
          'description': forms.Textarea(attrs={'rows':15, 'cols':120}),
        }

class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ['description']
        widgets = {
          'description': forms.Textarea(attrs={'rows':2, 'cols':90}),
        }

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['description']
        widgets = {
          'description': forms.Textarea(attrs={'rows':2, 'cols':90}),
        }

class AnswerCommentForm(ModelForm):
    class Meta:
        model = CommentAnswer
        fields = ['description']
        widgets = {
          'description': forms.Textarea(attrs={'rows':1, 'cols':40}),
        }

class CreateUserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = True
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']