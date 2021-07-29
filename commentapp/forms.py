from django.forms import ModelForm

from articleapp.models import Article


class CommentCreationForm(ModelForm):
    class Meta:
        model = Article
        fields = ['content']
