from django.db import models

class Photos(models.Model):
    name = models.CharField(max_length=200)
    strengths = models.TextField()
    weaknesses = models.TextField()
    photo = models.ImageField(upload_to='Photos/static/images')

    def _str_(self):
        return f'{self.pk}. {self.name} - {self.strengths} - {self.weaknesses} - {self.photo}'
