from django.shortcuts import render, get_object_or_404
from . models import Movie, Director, Actor
from django.db.models import F, Sum, Max, Min, Count, Avg, Value
from django.http import HttpResponse
from django.views.generic import ListView, DetailView



# Create your views here.


def show_all_movie(request):
    # movies = Movie.objects.order_by(F('year').asc(nulls_first=True), 'rating')
    movies = Movie.objects.annotate(
        true_bool=Value(True),
        false_bool=Value(False),
        str_field=Value('Hello'),
        int_field=Value(123),
        new_budget=F('budget')+100).annotate(
        ffff=F('rating')*F('year')
    )
    agg = movies.aggregate(Avg('budget'), Max('rating'), Min('rating'), Count('id'))
    # for movie in movies:
    #     movie.save()
    return render(request, 'movie_app/all_movies.html', {
        'movies': movies,
        'agg': agg
    })


def show_one_movie(request, slug_movie: str):
    movie = get_object_or_404(Movie, slug=slug_movie)
    return render(request, 'movie_app/one_movie.html', {
        'movie': movie
    })

# def show_all_dirs(request):
#     directors = Director.objects.all()
#     return render(request, 'movie_app/all_directors.html', {
#         'directors': directors
#     })


class Show_all_dirs(ListView):
    template_name = 'movie_app/all_directors.html'
    model = Director
    context_object_name = 'directors'


# def show_one_dirs(request, ind):
#     # dir = Director.objects.all()[ind]
#     dir = get_object_or_404(Director, id=ind)
#     return render(request, 'movie_app/one_dir.html', {
#         'dir': dir
#     })

class DetailDirector(DetailView):
    template_name = 'movie_app/one_dir.html'
    model = Director
    context_object_name = 'dir'
#
# def show_all_actors(request):
#     actors = Actor.objects.all()
#     return render(request, 'movie_app/all_actors.html', {
#         'actors': actors
#     })


class Show_all_actors(ListView):
    template_name = 'movie_app/all_actors.html'
    model = Actor
    context_object_name = 'actors'


# def show_one_actors(request, ind):
#     act = get_object_or_404(Actor, id=ind)
#     return render(request, 'movie_app/one_actor.html', {
#         'act': act
#     })

class DetailActor(DetailView):
    template_name = 'movie_app/one_actor.html'
    model = Actor
    context_object_name = 'act'
