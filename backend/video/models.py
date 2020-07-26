from django.db import models
from django.utils import timezone
from django.conf import settings
from .validators import validate_is_video, validate_is_thumbnail
from django.dispatch import receiver
from django.db.models.signals import post_delete


class VideoContent(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=True)
    thumbnail = models.ImageField(upload_to='thumbnail/', null=True, blank=True, validators=[validate_is_thumbnail])
    video = models.FileField(upload_to='video-list/', null=True, blank=True, validators=[validate_is_video])
    uploaded_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


# 画像と動画モデルを削除時にmediaファイルの画像と動画ファイルを削除する
@receiver(post_delete, sender=VideoContent)
def delete_file(sender, instance, **kwargs):
    instance.thumbnail.delete(False)
    instance.video.delete(False)


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
