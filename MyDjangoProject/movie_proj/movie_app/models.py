from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Director(models.Model):
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    director_email = models.EmailField()

    def __str__(self):
        return f'{self.f_name} {self.l_name}'

    def get_url(self):
        return reverse('one_dir', args=[self.id])


class DressingRoom(models.Model):
    floor = models.IntegerField()
    number = models.IntegerField()

    def __str__(self):
        return f'{self.floor} {self.number}'


class Actor(models.Model):
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    MALE = 'M'
    FEMALE = 'F'
    GENDERS = [
        (MALE, 'Мужчина'),
        (FEMALE, 'Женщина'),
    ]
    gender = models.CharField(max_length=1, choices=GENDERS, default=MALE)
    dressing = models.OneToOneField(DressingRoom, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        if self.gender == self.MALE:
            return f'Актер {self.f_name} {self.l_name}'
        else:
            return f'Актриса {self.f_name} {self.l_name}'

    def get_url(self):
        return reverse('one_actors', args=[self.id])


class Movie(models.Model):
    EUR = 'EUR'
    USD = 'USD'
    RUB = 'RUB'
    CURRENCY_CHOICE = [
        (EUR, 'Euro'),
        (USD, 'Dollars'),
        (RUB, 'Rubles')
    ]
    name = models.CharField(max_length=40)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    year = models.IntegerField(null=True, blank=True)
    budget = models.IntegerField(default=1000000, validators=[MinValueValidator(1)])
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICE, default=RUB)
    slug = models.SlugField(default='', null=False, db_index=True)
    director = models.ForeignKey(Director, on_delete=models.CASCADE, null=True, related_name='movies')
    actors = models.ManyToManyField(Actor)


    def __str__(self):
        return f'{self.name} - {self.rating}%'


    def get_url(self):
        return reverse('movie-detail', args=[self.slug])

    # def save(self, *args, **kwargs):
    #     self.slag = slugify(self.name)
    #     super(Movie, self).save(*args, **kwargs)



# python manage.py shell_plus --print-sql
# from movie_app.models import Movie
# Movie.objects.all()
# a = Movie.objects.all()[0]
# a.save()

# python3 manage.py makemigrations
# python3 manage.py migrate

# Movie.objects.get(id=5)
# Movie.objects.filter(budget=1000000)

