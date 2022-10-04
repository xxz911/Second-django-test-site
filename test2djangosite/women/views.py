from turtle import home
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound
from .models import *


menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]

def index(request):
    post = Women.objects.all()
    return render(request, 'women/index.html', {'post':post, 'menu': menu, 'title': 'Главная страница'})

def about(request):
    return render(request, 'women/about.html', {'menu': menu,'title': 'О сайте'})

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