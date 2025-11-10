from django.shortcuts import render
from django.http import HttpResponse
from .models import Tarefa
from .models import Alunos

def home(request):
   todas_as_tarefas = Tarefa.objects.all()
   todos_alunos = Alunos.objects.all()
   context = {
       'nome_usuario': 'João',
       'tecnologias': {'Python', 'Django', 'HTML', 'CSS'},
       'tarefas': todas_as_tarefas,
       'alunos': todos_alunos
   }
   #return HttpResponse("<h1>Olá, Mundo! Esta é minha primeira página Django!</h1>")
   return render(request, 'home.html', context)

def login(request):
    return HttpResponse("<input>Login</input>")



