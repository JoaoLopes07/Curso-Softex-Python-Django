from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Tarefa
from .models import Alunos
from .forms import TarefaForm

def home(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TarefaForm() 
    

    todas_as_tarefas = Tarefa.objects.all().order_by('-criada_em')
    todos_alunos = Alunos.objects.all()
    context = {
        'nome_usuario': 'João',
        'tecnologias': {'Python', 'Django', 'HTML', 'CSS'},
        'tarefas': todas_as_tarefas,
        'form': form,
        'alunos': todos_alunos
    }
    return render(request, 'home.html', context)

def login(request):
    return HttpResponse("<input>Login</input>")

def concluir_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    if request.method == 'POST':
        tarefa.concluida = True
        tarefa.save()
        return redirect('home')
def deletar_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    if request.method == 'POST':
        tarefa.delete()
        return redirect('home')