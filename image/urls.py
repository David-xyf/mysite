from django.urls import path

from image import views

app_name = 'image'
urlpattern = [
    path('list-images', views.list_images, name="list-images"),
    path('upload-image', views.upload_image, name="upload_image"),
]
