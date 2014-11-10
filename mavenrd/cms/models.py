from django.db import models
from django.contrib.auth.models import User
from mavenrd import settings

# Create your models here.
class Page(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=100)
    content = models.TextField()
    slug = models.SlugField(unique=True)
    active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    template = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title

class Post(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=100)
    content = models.TextField()
    slug = models.SlugField(unique=True)
    active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    template = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title

class UploadedMedia(models.Model):
    filename = models.CharField(max_length=100)
    file = models.FileField(upload_to=settings.FILE_UPLOADS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class MediaCollection(models.Model):
    name = models.CharField(max_length=100)
    media = models.ManyToManyField(UploadedMedia)
