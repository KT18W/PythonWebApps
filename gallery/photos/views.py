from pathlib import Path
from django.views.generic import TemplateView

class PhotoView(TemplateView):
    template_name = 'photo.html'

    def get_context_data(self, **kwargs):
        return {'photo':"/static\images\batman.jpg"}

