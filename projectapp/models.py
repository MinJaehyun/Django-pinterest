from django.db import models


class Project(models.Model):
    title       = models.CharField(max_length=100)
    description = models.TextField()  # TODO: CharField() 설정했는데, Text로 진행해보기
    image       = models.ImageField(upload_to='project/%Y%m%d')  # media/project/날짜
    created_at  = models.DateTimeField(auto_now_add=True)
