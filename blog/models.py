from django.db import models
from django.conf import settings
from django.db import models
from django.utils import timezone
from datetime import datetime


class Category(models.Model):
    name = models.CharField(max_length=20)

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    main_photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=True)
    categories = models.ManyToManyField('Category', related_name='posts')

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)