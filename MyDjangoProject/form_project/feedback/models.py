from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.


class Feedback(models.Model):
    name = models.CharField(max_length=10, validators=[MinLengthValidator(2)])
    surname = models.CharField(max_length=60, validators=[MinLengthValidator(3)])
    feedback = models.TextField()
    rating = models.PositiveIntegerField()


# python3 manage.py makemigrations
# python3 manage.py migrate

