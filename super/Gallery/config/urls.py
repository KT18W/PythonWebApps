from django.views.generic import RedirectView
from django.contrib import admin
from django.urls import path

from photos.views import PhotoDetailView, PhotoListView


urlpatterns = [

    #database
    path('admin/', admin.site.urls),
    # Photos
    path('', PhotoListView.as_view()),
    path('<int:id>', PhotoDetailView.as_view()),
]
