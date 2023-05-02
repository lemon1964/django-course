from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from dataclasses import dataclass
from django.template.loader import render_to_string

# Create your views here.

# def leo(request):
#     return HttpResponse("Знак зодиака Лев")
#
# def scorpio(request):
#     return HttpResponse("Знак зодиака Скорпион")
#
# def aries(request):
#     return HttpResponse("Знак зодиака Овен")
#
# def taurus(request):
#     return HttpResponse("Знак зодиака Телец")
#
# def gemini(request):
#     return HttpResponse("Знак зодиака Близнецы")
#
# def cancer(request):
#     return HttpResponse("Знак зодиака Рак")
#
# def virgo(request):
#     return HttpResponse("Знак зодиака Дева")
#
# def libra(request):
#     return HttpResponse("Знак зодиака Весы")
#
# def sagittarius(request):
#     return HttpResponse("Знак зодиака Стрелец")
#
# def capricorn(request):
#     return HttpResponse("Знак зодиака Козерог")
#
# def aquarius(request):
#     return HttpResponse("Знак зодиака Водолей")
#
# def pisces(request):
#     return HttpResponse("Знак зодиака Рыба")
# ---------
# def get_info_about_sign_zodiac(request, sign_zodiac):
#     signs = {
#         "aries": "Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).",
#         "taurus": "Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).",
#         "gemini": "Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).",
#         "cancer": "Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).",
#         "leo": "Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).",
#         "virgo": "Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).",
#         "libra": "Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).",
#         "scorpio": "Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).",
#         "sagittarius": "Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).",
#         "capricorn": "Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).",
#         "aquarius": "Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).",
#         "pisces": "Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта)."
#     }
#
#     if sign_zodiac.lower() in signs:
#         return HttpResponse(signs[sign_zodiac.lower()])
#     return HttpResponseNotFound(f"Неизвестный знак Зодиака - {sign_zodiac}")
# -----------
signs = {
    "aries": "Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).",
    "taurus": "Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).",
    "gemini": "Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).",
    "cancer": "Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).",
    "leo": "Лев - <i>пятый знак зодиака</i>, солнце (с 23 июля по 21 августа).",
    "virgo": "Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).",
    "libra": "Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).",
    "scorpio": "Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).",
    "sagittarius": "Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).",
    "capricorn": "Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).",
    "aquarius": "Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).",
    "pisces": "Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта)."
}
zodiacs = list(signs)

sign_types = {
    'fire': ['aries', 'leo', 'sagittarius'],
    'earth': ['taurus', 'virgo', 'capricorn'],
    'air': ['gemini', 'libra', 'aquarius'],
    'water': ['cancer', 'scorpio', 'pisces']
}
sign_types_lst = list(sign_types)

# def index(request):
#     # zodiacs = list(signs)
#     li_elements = ''
#     for sign in zodiacs:
#         redirect_path = reverse('horoscope-name', args=[sign])
#         li_elements += f"<li> <a href='{redirect_path}'> {sign.title()} </a> </li>"
#     responce = f'''
#     <ul>
#         {li_elements}
#     </ul>
#     '''
#     return HttpResponse(responce)

def index(request):
    context = {
        'zodiacs': zodiacs
    }
    return render(request, 'horoscope/index.html', context=context)


# def get_info_about_sign_zodiac(request, sign_zodiac: str):
#     descr = signs.get(sign_zodiac, None)
#     if descr:
#         return HttpResponse(f'<h2>{descr}</h2>')
#     else:
#         return HttpResponseNotFound(f"Неизвестный знак Зодиака - {sign_zodiac}")

# def get_info_about_sign_zodiac(request, sign_zodiac: str):
#     response = render_to_string('horoscope/info_zodiac.html')
#     return HttpResponse(response)

# @dataclass()
# class Person:
#     name: str
#     age: int
#
#     def __str__(self):
#         return f'{self.name}'

def get_info_about_sign_zodiac(request, sign_zodiac: str):
    descr = signs.get(sign_zodiac, None)
    data = {
        'description': descr,
        'sign': sign_zodiac,
        # 'sign_name': descr.split()[0],
        # 'zodiacs': zodiacs,
        'zodiacs': signs
        # 'intt': 111,
        # 'listt': [1, 2, 3],
        # 'kort': (5, 6, 7, 8),
        # 'dictt': {'name': 'Mic', 'age': 40},
        # 'my_class': Person('Bill', 55),
        # 'value': []
    }
    return render(request, 'horoscope/info_zodiac.html', context=data)

# def get_info_about_sign_zodiac_num(request, sign_zodiac: int):
#     return HttpResponse(f"This is the number {sign_zodiac}")
#
# def get_info_about_sign_zodiac_num(request, sign_zodiac: int):
#     if not 1 <= sign_zodiac <= 12:
#         return HttpResponseNotFound(f"Неправильный порядковый номер знака зодиака - {sign_zodiac}")
#     zodiacs = list(signs)[sign_zodiac - 1]
#     return HttpResponseRedirect(f'/horoscope/{zodiacs}')


def get_info_about_sign_zodiac_num(request, sign_zodiac: int):
    if not 1 <= sign_zodiac <= 12:
        return HttpResponseNotFound(f"Неправильный порядковый номер знака зодиака - {sign_zodiac}")
    zodiac = zodiacs[sign_zodiac - 1]
    redirect_url = reverse('horoscope-name', args=[zodiac])
    return HttpResponseRedirect(redirect_url)


def index_type(request):
    li_elements = ''
    for sign in sign_types_lst:
        redirect_path = reverse('type-name', args=[sign])
        li_elements += f"<li> <a href='{redirect_path}'> {sign.title()} </a> </li>"
    responce = f'''
    <ul>
        {li_elements}
    </ul>
    '''
    return HttpResponse(responce)


def get_info_about_sign_type(request, sign_type: str):
    descr = sign_types.get(sign_type, None)
    if descr:
        li_elements = ''
        for sign in descr:
            redirect_path = reverse('horoscope-name', args=[sign])
            li_elements += f"<li> <a href='{redirect_path}'> {sign.title()} </a> </li>"
        responce = f'''
        <ul>
            {li_elements}
        </ul> 
        '''
        return HttpResponse(responce)
    else:
        return HttpResponseNotFound(f"Неизвестный знак Стихии - {sign_type}")


def get_info_sign_zodiac(request, month, day):
    m = zodiacs[10:] + zodiacs[:10]
    d = (20, 19, 21, 20, 21, 22, 23, 23, 23, 24, 23, 22)
    month = month-1
    if day > d[month]:
        sign = m[month]
    else:
        sign = m[month-1]
    re_dir = reverse('horoscope-name', args=[sign])
    return HttpResponseRedirect(re_dir)


def get_yyyy_converters(request, sign_zodiac):
    return HttpResponse(f'Вы передали число из 4-х цифр - {sign_zodiac}')


def get_my_float_converters(request, sign_zodiac):
    return HttpResponse(f'Вы передали вещественное число - {sign_zodiac}')


def get_my_date_converters(request, sign_zodiac):
    return HttpResponse(f'Вы передали дату - {sign_zodiac}')



