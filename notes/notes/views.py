from django.views.generic import TemplateView
from .models import Notes


class NoteListView(TemplateView):
    template_name = 'notes.html'

    def get_context_data(self, **kwargs):
        return {
            'object_list': Notes.objects.all()
        }


class NoteDetailView(TemplateView):
    template_name = 'note.html'

    def get_context_data(self, **kwargs):
        return {
            'note': Notes.objects.get(pk=kwargs['pk'])
        }