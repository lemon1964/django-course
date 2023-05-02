from django.urls import path
from . import views

urlpatterns = [
    path("rectangle/<int:w>/<int:h>/", views.get_rectangle_area, name='rectangle'),
    path("square/<int:s>/", views.get_square_area, name='square'),
    path("circle/<int:r>/", views.get_circle_area, name='circle'),
    path("get_rectangle_area/<int:w>/<int:h>/", views.get_rectangle_area_redir),
    path("get_square_area/<int:s>/", views.get_square_area_redir),
    path("get_circle_area/<int:r>/", views.get_circle_area_redir),
    path("rectangle", views.get_fige),
    path("square", views.get_fige),
    path("circle", views.get_fige),
]