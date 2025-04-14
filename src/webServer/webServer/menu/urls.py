from django.urls import path

from . import views

urlpatterns: list = [
    path('', views.menu, name= "menu"),
    path('info/', views.info, name= 'info')
]
