from django.forms import ModelForm

from commentapp.models import Comment


class CommentCreationForm(ModelForm):
    class Meta:
        model = Comment       # FIXME: Article 에서 Comment 로 수정
        fields = ['content']
