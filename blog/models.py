from django.db import models
from django.conf import settings
from django.db import models
from django.utils import timezone
from datetime import datetime
from django.contrib.auth.models import User
from categories.models import Category

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    main_photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
   

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
   


    def __str__(self):
        return self.text

