from django import forms
from .models import VideoContent, ImageContent


class VideoForm(forms.ModelForm):
    class Meta:
        model = VideoContent
        fields = ('title','video',)


class ImageForm(forms.ModelForm):
    class Meta:
        model = ImageContent
        fields = ('title','image')
