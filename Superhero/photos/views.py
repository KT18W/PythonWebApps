from pathlib import Path
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, DeleteView, UpdateView
from .models import Hero
from .models import Photo
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class PhotoListView(TemplateView):
    template_name = 'photos.html'
    def get_context_data(self, **kwargs):
        return {
            'object_list': Hero.objects.all()
        }

class NotesView(TemplateView):
    template_name = 'notes.html'
    def get_context_data(self, **kwargs):
        return {
            'object_list': Hero.objects.all()
        }

class CarouselView(TemplateView):
    template_name = 'carousel.html'

    def get_context_data(self, **kwargs):
        photos = Hero.objects.all()
        carousel = carousel_data(photos)
        return dict(title='Carousel View', carousel=carousel)


def carousel_data(photos):

    def photo_data(id, image):
        x = dict(image_url=f"/media/{Hero.photo}", id=str(id), label=f"{Hero.photo} {id}")
        if id == 0:
            x.update(active="active", aria='aria-current="true"')
        return x

    return [photo_data(id, Hero.pk) for id, Hero.photo in enumerate(photos)]

class PhotoDetailView(TemplateView):
    template_name = 'photo.html'

    def get_context_data(self, **kwargs):
        i = kwargs['id']
        return dict(hero=Hero.objects.get(pk=i))


class HeroCreateView(LoginRequiredMixin, CreateView):  
    template_name = "add.html"
    model = Hero
    fields = '__all__'

class HeroUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "edit.html"
    model = Hero
    fields = '__all__'


class HeroDeleteView(LoginRequiredMixin, DeleteView):
    model = Hero
    template_name = 'delete.html'
    success_url = reverse_lazy('hero_list')

class AuthorAddView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/account_add.html'



