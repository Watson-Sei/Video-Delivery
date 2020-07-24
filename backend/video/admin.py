from django.contrib import admin
from .models import ImageContent, VideoContent, Comment


admin.site.register(VideoContent)
admin.site.register(ImageContent)
admin.site.register(Comment)