from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# def table(request):
#     responce = 'Текст'
#     return HttpResponse(responce)

# def table(request):
#     context = {
#         'zodiacs': [1, 2, 3]
#     }
#     return render(request, 'table/info_table.html', context=context)

def table(request):
    return render(request, 'table/info_table.html')

def filtered(request):
    return render(request, 'table/filtered.html')

def plan(request):
    return render(request, 'table/plan.html')

