from django.db import models

class Notes(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self):
        return f'{self.pk}. {self.title} - {self.author}'