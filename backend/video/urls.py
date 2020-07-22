from django.urls import path
from video.views import home, modelform_upload,imageform_upload

urlpatterns = [
    path('home/', home, name='home'),
    path('modelform_upload/', modelform_upload, name='modelform_upload'),
    path('imageform_upload/', imageform_upload, name='imageform_upload')
]
