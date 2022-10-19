# Generated by Django 4.1 on 2022-10-19 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0005_alter_photos_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('strengths', models.TextField()),
                ('weaknesses', models.TextField()),
                ('photo', models.CharField(default='/static/images/bad.jpg', max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Photos',
        ),
    ]