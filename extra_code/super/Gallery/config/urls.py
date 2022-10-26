from django.views.generic import RedirectView
from django.contrib import admin
from django.urls import path

from photos.views import PhotoDetailView, PhotoListView, HeroCreateView, HeroDeleteView, HeroUpdateView


urlpatterns = [

    #database
    path('admin/', admin.site.urls),
    # Photos
    path('', PhotoListView.as_view()),
    path('<int:id>', PhotoDetailView.as_view()),
    path('add', HeroCreateView.as_view(),  name='add'),
    path('<int:pk>/edit', HeroUpdateView.as_view(),  name='edit'),
    path('<int:pk>/delete', HeroDeleteView.as_view(),  name='delete'),
]
