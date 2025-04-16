from django.http import HttpResponse
from django.shortcuts import render

from .models import App


def menu(request) -> HttpResponse:
    context: dict = {
        'appsList': App.objects.all()
    }
    return render(request, 'menu/index.html', context)

def info(request) -> HttpResponse:
    return HttpResponse('Web server menu info')
