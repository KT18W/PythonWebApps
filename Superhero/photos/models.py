from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse_lazy

class Hero(models.Model):
    name = models.CharField(max_length=200, default='name')
    strengths = models.TextField(max_length=500, default='strengths')
    weaknesses = models.TextField(max_length=500, default='weaknesses')
    identity = models.TextField(max_length=200, default='identity')
    description = models.TextField(max_length=2000, default='description')
    photo = models.CharField(max_length=200, default='/static/images/bad.jpg')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('hero_list')

class Author(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, editable=False)
    bio = models.TextField()

    def __str__(self):
        return f'{self.user.username}'
    
