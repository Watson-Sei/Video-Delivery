from django import forms
from .models import VideoContent, ImageContent, Comment


class VideoForm(forms.ModelForm):
    class Meta:
        model = VideoContent
        fields = ('title','thumbnail','video',)


class ImageForm(forms.ModelForm):
    class Meta:
        model = ImageContent
        fields = ('title','image')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
