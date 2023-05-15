from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    body = models.TextField()
    weather = models.CharField(max_length=10, default=None, null=True)
    video = models.CharField(max_length=100, default=None, null=True)
    image = models.ImageField(upload_to="post/", blank=True, null=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:20]
