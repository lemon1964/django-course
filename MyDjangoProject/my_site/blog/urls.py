from django.urls import path
from . import views

#
# urlpatterns = [
#     path("posts/", views.posts),
#     path("", views.empty),
# ]
urlpatterns = [
    path("", views.posts),
    path("keanu", views.keanu),
    path("records", views.get_guinness_world_records),
    path("people", views.people),
    path("people2", views.people_detail),
    path("<int:info>/", views.about_info_int),
    path("<info>/", views.about_info),
]
