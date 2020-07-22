from django.shortcuts import render, redirect
from .models import VideoContent, ImageContent
from .forms import VideoForm, ImageForm
from django.contrib.auth.decorators import login_required

@login_required
def modelform_upload(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = VideoForm(request.POST)
    return render(request, 'video/upload.html', {'form': form})

@login_required
def imageform_upload(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ImageForm(request.POST)
    return render(request, 'video/image_upload.html', {'form': form})

@login_required
def home(request):
    return render(request, 'video/home.html')
