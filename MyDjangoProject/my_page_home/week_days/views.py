from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

# def monday(request):
#     s = f'<li>http://127.0.0.1:8000/todo_week/monday</li> <li>Дела раз</li> <li>Дела два</li> <li>Дела три</li>'
#     return HttpResponse(s)
#
# def tuesday(request):
#     return HttpResponse("Дел еще больше")
dict_day = {
    'monday': 'Составляем план на неделю',
    'tuesday': 'Пишем план на неделю',
    'wednesday': 'Редактируем план на неделю',
    'thursday': 'Согласуем план на неделю',
    'friday': 'Вешаем план на стенку',
    'saturday': 'Делаем пометки в плане',
    'sunday': 'Обдумываем новый план',
}


# def get_day(request, day: str):
#     if day.lower() in dict_day:
#         return HttpResponse(dict_day[day.lower()])
#     return HttpResponseNotFound(f"Нет такого дня в неделе - {day}")
def get_day(request, day: str):
    return render(request, 'week_days/greeting.html')


# def get_day_num(request, day: int):
#     if 1 <= day <= 7:
#         return HttpResponse(f'Сегодня {day} день недели')
#     else:
#         return HttpResponse(f'Неверный номер дня - {day}')

def get_day_num(request, day: int):
    if not 1 <= day <= 7:
        return HttpResponse(f'Неверный номер дня - {day}')
    day_ind = list(dict_day)[day - 1]
    redirect_num = reverse('week_day_name', args=[day_ind])
    return HttpResponseRedirect(redirect_num)








