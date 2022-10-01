from turtle import home
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound

def index(request):
    return HttpResponse("Страница приложения women.")

def categories(request, catid):
    if request.POST:
        print(request.POST)
    return HttpResponse(f"<h1>Статьи по котегориям</h1><p>{catid}</p>")

def archive(request, year):
    if int(year) > 2020:
        return redirect(home, permanent=True)

    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена!</h1>')