from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200)
    writer = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    pub_date = models.DateTimeField()
    body = models.TextField()
    weather = models.CharField(max_length=10, default=None, null=True)
    video = models.CharField(max_length=100, default=None, null=True)
    image = models.ImageField(upload_to="post/", blank=True, null=True)
    like = models.ManyToManyField(User, related_name='likes', blank=True)
    like_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:20]

class Comment(models.Model):
    content = models.TextField()
    pub_date = models.DateTimeField()
    writer = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.post.title+" : "+self.content[:20]