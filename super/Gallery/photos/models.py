from django.db import models

class Hero(models.Model):
    name = models.CharField(max_length=200)
    strengths = models.TextField()
    weaknesses = models.TextField()
    photo = models.CharField(max_length=200, default='/static/images/bad.jpg')

    def __str__(self):
        return f'{self.pk}. {self.name}'
