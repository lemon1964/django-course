from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=70)
    rating = models.IntegerField()
    is_best_selling = models.BooleanField()
    author = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f'{self.title} - {self.rating}%'


# python manage.py shell_plus --print-sql
# from book_app.models import Book
# Book.objects.all()
# a = Book.objects.all()[0]
# a.save()

# python3 manage.py makemigrations
# python3 manage.py migrate
#


