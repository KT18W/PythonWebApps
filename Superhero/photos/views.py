from pathlib import Path
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, DeleteView, UpdateView
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


class HeroCreateView(CreateView):
    template_name = "add.html"
    model = Hero
    fields = '__all__'

class HeroUpdateView(UpdateView):
    template_name = "edit.html"
    model = Hero
    fields = '__all__'


class HeroDeleteView(DeleteView):
    model = Hero
    template_name = 'delete.html'
    success_url = reverse_lazy('hero_list')



