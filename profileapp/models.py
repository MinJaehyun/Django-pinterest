from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField(upload_to='profile/%Y%m%d', null=True)
    nickname = models.CharField(max_length=50, unique=True, null=True)
    message = models.TextField(max_length=500, null=True)
