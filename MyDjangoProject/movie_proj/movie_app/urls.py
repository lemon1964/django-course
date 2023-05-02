from django.contrib import admin
from django.urls import path
from . import views
from django.urls import path, include


urlpatterns = [
    path("", views.show_all_movie),
    path("movie/<slug:slug_movie>", views.show_one_movie, name='movie-detail'),
    path('__debug__/', include('debug_toolbar.urls')),
    path("directors", views.Show_all_dirs.as_view(), name='all_dirs'),
    path("directors/<int:pk>", views.DetailDirector.as_view(), name='one_dir'),
    path("actors", views.Show_all_actors.as_view(), name='all_actors'),
    path("actors/<int:pk>", views.DetailActor.as_view(), name='one_actors'),

]

