from django.urls import path
from .views import  home, modelform_upload, imageform_upload,video_detail, add_comment_to_video

urlpatterns = [
    path('home/', home, name='home'),
    path('modelform_upload/', modelform_upload, name='modelform_upload'),
    path('imageform_upload/', imageform_upload, name='imageform_upload'),
    path('video/<int:pk>/', video_detail, name='video_detail'),
    path('video/<int:pk>/comment/', add_comment_to_video, name='add_comment_to_video'),
]
