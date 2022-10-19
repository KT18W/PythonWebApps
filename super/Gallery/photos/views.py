from pathlib import Path
from django.views.generic import TemplateView
from .models import Hero


class PhotoListView(TemplateView):
    template_name = 'photos.html'
    
    def get_context_data(self, **kwargs):
        return {
            'object_list': Hero.objects.all()
        }


class PhotoDetailView(TemplateView):
    template_name = 'photo.html'

    def get_context_data(self, **kwargs):
        i = kwargs['id']
        return dict(hero=Hero.objects.get(pk=i))


