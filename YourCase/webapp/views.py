from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    context = {
        'title': 'Главная страница'
    }
    return render(request, 'webapp/index.html', context=context)
