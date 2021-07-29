from django.contrib.auth.models import User
from django.db import models


class Article(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='article', null=True)
    title = models.CharField(max_length=200, null=True)
    content = models.TextField(null=True)
    image = models.ImageField(upload_to='article/%Y%m%d')  # TODO: null=False 지정 안하고 실행 해보기
    created_at = models.DateTimeField(auto_now_add=True)
