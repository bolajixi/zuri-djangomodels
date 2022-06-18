from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

User = get_user_model()

class Post(models.Model):
    """Model definition for Post."""

    title = models.CharField(max_length=200)
    title = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(auto_now=True)
