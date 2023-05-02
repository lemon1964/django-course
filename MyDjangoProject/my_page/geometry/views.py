from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from math import pi

# Create your views here.


def get_rectangle_area(request, w, h):
    ar = w * h
    return HttpResponse(f'Площадь прямоугольника размером {w}x{h} равна {ar}')


def get_square_area(request, s):
    ar = s ** 2
    return HttpResponse(f'Площадь квадрата размером {s}x{s} равна {ar}')


def get_circle_area(request, r):
    ar = round(pi * r ** 2, 1)
    return HttpResponse(f'Площадь круга радиуса {r} равна {ar}')


def get_rectangle_area_redir(request, w, h):
    re_dir = reverse('rectangle', args=[w, h])
    return HttpResponseRedirect(re_dir)


def get_square_area_redir(request, s):
    re_dir = reverse('square', args=[s])
    return HttpResponseRedirect(re_dir)


def get_circle_area_redir(request, r):
    re_dir = reverse('circle', args=[r])
    return HttpResponseRedirect(re_dir)


def get_fige(request):
    a = request.path.split('/')[-1]
    return render(request, f'geometry/{a}.html')

