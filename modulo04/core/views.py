from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Olá, Mundo! Esta é minha primeira página Django!</h1>")

def home2(request):
    return HttpResponse("<h1>Meu primeiro código em Django</h1>")

