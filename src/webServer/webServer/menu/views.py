from django.http import HttpResponse
from django.shortcuts import render


def menu(request) -> HttpResponse:
    return HttpResponse('Web server menu')

def info(request) -> HttpResponse:
    return HttpResponse('Web server menu info')
