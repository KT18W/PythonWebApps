from django.views.generic import RedirectView
from django.contrib import admin
from django.urls import path

from photos.views import PhotoDetailView, PhotoListView


urlpatterns = [

    # Home
    path('', RedirectView.as_view(url='photo/')),

    #database
    path('admin/', admin.site.urls),
    # Photos
    path('photo/', PhotoListView.as_view()),
    path('photo/<int:id>', PhotoDetailView.as_view()),
]
