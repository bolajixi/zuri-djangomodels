from django.conf import settings
from django.db import models

# Create your models here.

class Post(models.Model):
    """Model definition for Post."""

    title = models.CharField(max_length=200)
    title = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    created_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(auto_now=True)
