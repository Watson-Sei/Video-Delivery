from django.shortcuts import render, redirect
from .models import VideoContent, ImageContent
from .forms import VideoForm, ImageForm


def modelform_upload(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = VideoForm(request.POST)
    return render(request, 'video/upload.html', {'form': form})


def imageform_upload(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ImageForm(request.POST)
    return render(request, 'video/image_upload.html', {'form': form})


def index(request):
    return render(request, 'video/index.html')
