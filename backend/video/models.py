from django.db import models
from django.utils import timezone


class VideoContent(models.Model):
    title = models.CharField(max_length=50, blank=True)
    video = models.FileField(upload_to='video-list/',null=True, blank=True)
    uploaded_at = models.DateTimeField(default=timezone.now)


class ImageContent(models.Model):
    title = models.CharField(max_length=50, blank=True, default='test')
    image = models.ImageField(upload_to='image-list/')
    uploaded_at = models.DateTimeField(default=timezone.now)
