from django.urls import path
from video.views import index, modelform_upload,imageform_upload

urlpatterns = [
    path('', index, name='index'),
    path('modelform_upload/', modelform_upload, name='modelform_upload'),
    path('imageform_upload/', imageform_upload, name='imageform_upload')
]
