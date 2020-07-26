from django.shortcuts import render, redirect, get_object_or_404
from .models import VideoContent, ImageContent, Comment
from .forms import VideoForm, ImageForm, CommentForm
from django.contrib.auth.decorators import login_required


# import cv2
# import os
# from .thumbnail import make_thumbnail


@login_required
def modelform_upload(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save(commit=False)
            video.author = request.user
            video.save()
            return redirect('home')
    else:
        form = VideoForm()
    return render(request, 'video/upload.html', {'form': form})


@login_required
def imageform_upload(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ImageForm()
    return render(request, 'video/image_upload.html', {'form': form})


@login_required
def home(request):
    if request.method == 'POST':
        context = {
            'username': request.user,
            'video_list': VideoContent.objects.filter(title__icontains=request.POST['search'])
        }

    else:
        context = {
            'username': request.user,
            'video_list': VideoContent.objects.all()
        }
    return render(request, 'video/home.html', context)


@login_required
def video_detail(request, pk):
    video = get_object_or_404(VideoContent, pk=pk)
    return render(request, 'video/video_detail.html', {'video': video})


@login_required
def add_comment_to_video(request, pk):
    video = get_object_or_404(VideoContent, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.video_content = video
            comment.save()
            return redirect('video_detail', pk=video.pk)
    else:
        form = CommentForm()
    return render(request, 'video/add_comment_to_video.html', {'form': form})


@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('video_detail', pk=comment.video_content.pk)


@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('video_detail', pk=comment.video_content.pk)
