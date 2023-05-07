from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)


class Category(models.Model):
    name = models.CharField(max_length=255)

