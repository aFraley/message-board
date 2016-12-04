from django.forms.models import ModelForm
from django.forms.widgets import TextInput

from .models import Comment, Topic


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = [
            'text'
        ]
        widgets = {
            'text': TextInput(attrs={
                'class': 'form-control',
                'autofocus': True
            })
        }


class TopicForm(ModelForm):
    class Meta:
        model = Topic
        fields = [
            'title'
        ]
