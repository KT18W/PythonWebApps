from django.views.generic import RedirectView
from django.contrib import admin
from django.urls import path, include

from photos.views import PhotoDetailView, PhotoListView, HeroCreateView, HeroDeleteView, HeroUpdateView, AuthorAddView


urlpatterns = [

    #database
    path('admin/', admin.site.urls),
    
    # Photos
    path('', PhotoListView.as_view(), name='hero_list'),
    path('<int:id>', PhotoDetailView.as_view(), name='detail_view'),
    path('add', HeroCreateView.as_view(),  name='add'),
    path('<int:pk>/edit', HeroUpdateView.as_view(),  name='edit'),
    path('<int:pk>/delete', HeroDeleteView.as_view(),  name='delete'),
    
    #user stuff
    path('accounts/', include('django.contrib.auth.urls')),
    path('author/add/', AuthorAddView.as_view(),     name='author_add'),
]
