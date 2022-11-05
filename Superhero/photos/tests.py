from django.test import SimpleTestCase, TestCase
from .models import Hero
from django.urls import reverse

class PhotosAppTest(SimpleTestCase):

    def test_django(self):
        self.assertTrue(True)

class PhotoDataTest(TestCase):
    def test_blog(self):
        Hero.objects.create(name = 'Name')
        self.assertTrue(Hero.objects.all())

        a = Hero.objects.get(pk = 1)
        self.assertEqual(a.name, 'Name')

        a.name = "New Name"
        a.save()
        self.assertEqual(a.name, 'New Name')

        a.delete()
        self.assertEqual(len(Hero.objects.all()), 0)

class PhotoListViewTest(TestCase):
    def test_photo_list_view(self):
        self.assertEqual(reverse("hero_list"), "/")

    