from django.contrib.auth import get_user_model
from django.db import models


class Post(models.Model):
    user = models.ForeignKey(get_user_model(), related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
