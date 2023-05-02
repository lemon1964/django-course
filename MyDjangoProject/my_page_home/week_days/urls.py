from django.urls import path
from . import views

# urlpatterns = [
#     path("monday/", views.monday),
#     path("tuesday/", views.tuesday),
# ]

urlpatterns = [
    path("<int:day>/", views.get_day_num),
    path("<str:day>/", views.get_day, name='week_day_name'),
]

