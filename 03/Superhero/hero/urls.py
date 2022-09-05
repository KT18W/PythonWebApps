from django.urls import path
from .views import BatmanView, SpidermanView, IndexView, GrootView

urlpatterns = [
    path('', IndexView.as_view()),
    path('spiderman', SpidermanView.as_view()),
    path('groot', GrootView.as_view()),
    path('batman', BatmanView.as_view()),
]
