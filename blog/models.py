from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    data_published = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    data_posted = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username + ' commented on ' + self.post.title


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
