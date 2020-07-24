from django.db import models
from django.utils import timezone
from django.conf import settings


class VideoContent(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=True)
    thumbnail = models.ImageField(upload_to='thumbnail/', blank=True)
    video = models.FileField(upload_to='video-list/',null=True, blank=True)
    uploaded_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class ImageContent(models.Model):
    title = models.CharField(max_length=50, blank=True, default='test')
    image = models.ImageField(upload_to='image-list/')
    uploaded_at = models.DateTimeField(default=timezone.now)


class Comment(models.Model):
    video_content = models.ForeignKey('video.VideoContent', on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

