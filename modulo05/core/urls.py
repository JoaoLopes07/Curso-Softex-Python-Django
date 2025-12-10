from django.urls import path
from .views import ListaTarefasAPIView, TarefasEstatisticasAPIView, DetalheTarefaAPIView, DuplicarTarefaAPIView

app_name = 'core'
urlpatterns = [

    path('tarefas/', ListaTarefasAPIView.as_view(), name='lista-tarefas'),
    path('tarefas/<int:pk>/', DetalheTarefaAPIView.as_view(), name='detalhe-tarefa'),
    path('tarefas/estatisticas/', TarefasEstatisticasAPIView.as_view()),
    path('tarefas/<int:pk>/duplicar/', DuplicarTarefaAPIView.as_view(), name='duplicar-tarefa'),
]