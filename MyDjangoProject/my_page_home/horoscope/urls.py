from django.urls import path
from . import views


urlpatterns = [
    path("<int:sign_zodiac>/", views.get_info_about_sign_zodiac_num),
    path("<str:sign_zodiac>/", views.get_info_about_sign_zodiac),
]