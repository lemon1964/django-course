from django.db import models

# Create your models here.


class Gallery(models.Model):
    image = models.FileField(upload_to='my_gallery')

# python3 manage.py makemigrations
# python3 manage.py migrate

