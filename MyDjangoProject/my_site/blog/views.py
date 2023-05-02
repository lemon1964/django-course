from django.shortcuts import render
from random import sample
from django.http import HttpResponse, HttpResponseNotFound
from django.template.loader import render_to_string


posts_ls = [
    {
        'title': 'Рыбалка',
        'description': 'Хорошо посидели',
        'date': '21 авг 2021',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Commodi distinctio doloremque et fuga iste neque, pariatur quod sit veritatis voluptates?'
    },
    {
        'title': 'Париж',
        'description': 'Незабываемое путешествие',
        'date': '5 сент 2020',
        'content': '''Lorem ipsum dolor sit amet, consectetur adipisicing elit. 
                Commodi distinctio doloremque et fuga iste neque, pariatur quod sit veritatis voluptates?'''
    },
    {
        'title': 'Финал лиги чемпионов',
        'description': 'Реал опять выиграл ЛЧ',
        'date': '28 мая 2022',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Qui, rem.'
    },
    {
        'title': 'Охота на уток',
        'description': 'Ни одна утка не пострадала',
        'date': '7 дек 2019',
        'content': 'Lorem ipsum dolor sit amet.'
    },
    {
        'title': 'Фестиваль огурца',
        'description': 'Суздаль ждет тебя',
        'date': '12 июль 2021',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Adipisci consectetur id inventore odit recusandae!'
    },
    {
        'title': 'Нашествие',
        'description': 'Даешь рок, но в следующем году',
        'date': '29 июль 2021',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Est mollitia recusandae rem?'
    },
    {
        'title': 'Новый год',
        'description': 'Эх, еще один год пролетел',
        'date': '31 дек 2022',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. A architecto corporis fuga ipsam laboriosam, nesciunt non quae qui ut veniam.'
    },
]

# def posts(request):
#     return HttpResponse("Все посты блога")
def posts(request):
    return render(request, 'blog/list_detail.html')

# def empty(request):
#     return HttpResponse("Главная страница")
    # response = render_to_string('blog/index.html')

# def empty(request):
#     # response = render_to_string('base.html')
#     response = render_to_string('blog/index.html')
#     return HttpResponse(response)
def empty(request):
    context = {
        'posts_ls': sample(posts_ls, 3)
    }
    return render(request, 'blog/index.html', context=context)


# def about_info(request, info):
#     return HttpResponseNotFound(f"Информация о посте {info}")
#
# def about_info_int(request, info):
#     return HttpResponseNotFound(f"Здесь содержится информация о посте под номером {info}")

def about_info(request, info):
    data = {
        'info': info,
    }
    return render(request, 'blog/detail_by_name.html', context=data)

def about_info_int(request, info):
    data = {
        'info': info,
    }
    return render(request, 'blog/detail_by_number.html', context=data)

def keanu(request):
    data = {
        'year_born': '1964 г.',
        'city_born': 'Бейрут',
        'movie_name': 'На гребне волны',
    }
    return render(request, 'blog/keanu.html', context=data)

def get_guinness_world_records(request):
    context = {
        'power_man': 'Narve Laeret',
        'bar_name': 'Bob’s BBQ & Grill',
        'count_needle': 1790,
    }
    return render(request, 'blog/guinnessworldrecords.html', context=context)

def people(request):
    people = [
        'Жукова Анна Константиновна',
        'Юлия Степановна Потапова',
        'Гущин Аполлинарий Тимурович',
        'Дорофей Ярославович Третьяков',
        'Селезнева Анна Тарасовна',
        'Федотов Симон Харлампьевич',
        'Красильникова Вера Борисовна',
        'Бажен Тихонович Костин',
        'Веселова Анжелика Тимофеевна',
        'Щербаков Самсон Феодосьевич'
    ]
    context = {
        'peoples': people
    }
    return render(request, 'blog/people.html', context=context)


def people_detail(request):
    people = [
        {'name': 'Жанна Ивановна Бобылева', 'age': 28, 'phone': '+72609577301'},
        {'name': 'Спиридон Феликсович Алексеев', 'age': 48, 'phone': '8 445 133 42 50'},
        {'name': 'Лыткина Зоя Рубеновна', 'age': 34, 'phone': '84061070300'},
        {'name': 'Олимпиада Святославовна Петухова', 'age': 70, 'phone': '8 740 992 96 95'},
        {'name': 'Лазарева Нина Кирилловна', 'age': 67, 'phone': '89040731989'},
        {'name': 'Каллистрат Ильич Ширяев', 'age': 63, 'phone': '+7 418 298 8976'},
        {'name': 'Евсеев Любосмысл Чеславович', 'age': 47, 'phone': '83111461302'},
        {'name': 'Прохор Харламович Артемьев', 'age': 47, 'phone': '+77827445919'},
        {'name': 'Кондрат Игнатьевич Ершов', 'age': 35, 'phone': '+7 419 594 39 00'},
        {'name': 'Ипат Власович Ильин', 'age': 47, 'phone': '88004779773'}
    ]
    context = {
        'peoples': people
    }
    return render(request, 'blog/people_detail.html', context=context)

