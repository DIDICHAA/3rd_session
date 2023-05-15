from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.TextField(max_length=10)
    department = models.TextField(null=True, max_length=30)
    email = models.TextField(null=True)
    track = models.CharField(null=True, max_length=10)




# Create your models here.
