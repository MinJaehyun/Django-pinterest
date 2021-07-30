from django.contrib.auth.models import User
from django.db import models

from articleapp.models import Article


class Comment(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='comment', null=True)  # FIXME: 추후 User 대체하기
    article = models.ForeignKey(Article, on_delete=models.SET_NULL, related_name='comment', null=True)
    content = models.TextField(null=False)  # TODO: null=False
    created_at = models.DateTimeField(auto_now_add=True)  # TODO: auto_now 로 설정한 이유?
