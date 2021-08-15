from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class BlogPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body_text = models.TextField(default=None, blank=True, null=True)
    created_at = models.DateTimeField(auto_now=False, blank=True)

    def __str__(self):
        return self.title + '|' + str(self.user)


class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True, blank=True)
    comment = models.TextField(default=None, blank=True, null=True)
 
    def __str__(self):
        return self.user
