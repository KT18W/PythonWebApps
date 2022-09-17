from django.contrib import admin
from django.urls import path
from gallery.photos.views import PhotoListView
from photos.views import PhotoView

urlpatterns = [
    path('<str:name>', PhotoView.as_view()),
    path('', PhotoListView.as_view()),
]
