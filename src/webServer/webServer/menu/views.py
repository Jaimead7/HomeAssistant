from dataclasses import dataclass

from django.http import HttpResponse
from django.shortcuts import render


def menu(request) -> HttpResponse:
    @dataclass
    class App:
        name: str
        url: str

    appsList: list[App] = [
        App('Weather', '/weather'),
        App('Clock', '/clock'),
    ]
    context: dict = {
        'appsList': appsList
    }
    return render(request, 'menu/index.html', context)

def info(request) -> HttpResponse:
    return HttpResponse('Web server menu info')
