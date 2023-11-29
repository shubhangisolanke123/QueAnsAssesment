# forms.py in the qanda app
from django import forms
from .models import Question, Answer,Like

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'content']

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['user','question','content']

class LikeForm(forms.ModelForm):
    class Meta:
        model = Like
        fields = ['user','answer']
