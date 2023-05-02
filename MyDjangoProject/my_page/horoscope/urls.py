from django.urls import path, register_converter
from . import views, converters

register_converter(converters.FourDigitYearConverter, 'yyyy')
register_converter(converters.My_Float_Converter, 'my_float')
register_converter(converters.MyDateConverter, 'my_date')

# urlpatterns = [
#     path("leo/", views.leo),
# ...
#     path("capricorn/", views.capricorn),
# ]


urlpatterns = [
    path('', views.index, name='horoscope-index'),
    path("<my_date:sign_zodiac>/", views.get_my_date_converters),
    path('type/', views.index_type),
    path('type/<str:sign_type>/', views.get_info_about_sign_type, name='type-name'),
    path('<int:month>/<int:day>/', views.get_info_sign_zodiac),
    path("<yyyy:sign_zodiac>/", views.get_yyyy_converters),
    path("<int:sign_zodiac>/", views.get_info_about_sign_zodiac_num, name='int-sign'),
    path("<my_float:sign_zodiac>/", views.get_my_float_converters),
    path("<str:sign_zodiac>/", views.get_info_about_sign_zodiac, name='horoscope-name'),
]
