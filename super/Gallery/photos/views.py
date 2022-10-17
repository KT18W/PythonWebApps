from pathlib import Path
from django.views.generic import TemplateView
from .models import Photos


def photo_list():
    def photo_details(i, f):
        c = {0 : 'Captain America', 1 : 'The Hulk', 2 : 'Iron Man', 3 : 'Superman', 4 : 'Thor'}
        caption = c[i]
        w = {0 : 'That girl', 1 : 'Night Time', 2 : 'A light rain', 3 : 'Kryptonite', 4 : 'Natalie Portman'}
        weakness = w[i]
        s = {0 : 'His Sheild', 1 : 'Emotions', 2 : 'Money', 3 : 'Flying', 4 : 'His hammer'}
        strength = s[i]
        return dict(id=i, file=f, caption=caption, weakness=weakness, strength=strength)

    photos = Path('static/images').iterdir()
    photos = [photo_details(i, f) for i, f in enumerate(photos)]
    return photos


class PhotoListView(TemplateView):
    template_name = 'photos.html'
    
    def get_context_data(self, **kwargs):
        return {
            'object_list': Photos.objects.all()
        }


class PhotoDetailView(TemplateView):
    template_name = 'photo.html'

    def get_context_data(self, **kwargs):
        i = kwargs['id']
        photos = photo_list()
        p = photos[i]
        return dict(photo=p)


