from django.contrib import admin
from django.urls import path
from notes.views import NoteDetailView, NoteListView

urlpatterns = [
    path('admin/', admin.site.urls),

    # Note
    path('', NoteListView.as_view()),
    path('<int:pk>', NoteDetailView.as_view()),
]
