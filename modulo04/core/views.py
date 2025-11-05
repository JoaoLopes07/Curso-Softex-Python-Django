from django.shortcuts import render
from django.http import HttpResponse

def home(request):
   context = {
       'nome_usuario': 'João',
       'tecnologias': {'Python', 'Django', 'HTML', 'CSS'}
   }
   #return HttpResponse("<h1>Olá, Mundo! Esta é minha primeira página Django!</h1>")
   return render(request, 'home.html', context)

def login(request):
    return HttpResponse("<input>Login</input>")



