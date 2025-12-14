from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Count
from .models import Tarefa
from .serializers import TarefaSerializer
from django.db import IntegrityError
import logging
from datetime import date

logger = logging.getLogger(__name__)


class ListaTarefasAPIView(APIView):

    def get(self, request, format=None):
        tarefas = Tarefa.objects.all()
        serializer = TarefaSerializer(tarefas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        try:
            serializer = TarefaSerializer(
                data=request.data,
                context={'request': request}
            )

            if serializer.is_valid():
                serializer.save()
                logger.info(f"[INFO]: Tarefa criada: {serializer.data['id']}")
                return Response(
                    serializer.data,
                    status=status.HTTP_201_CREATED
                )

            logger.warning(f"[WARNING]: Validação falhou: {serializer.errors}")
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

        except IntegrityError:
            return Response(
                {'error': 'Violação de integridade no banco de dados.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        except Exception as e:
            logger.error(f"Erro ao criar tarefa: {str(e)}")
            return Response(
                {'error': 'Erro interno do servidor.'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class TarefasEstatisticasAPIView(APIView):
    def get(self, request):
        total = Tarefa.objects.count()
        concluidas = Tarefa.objects.filter(concluida=True).count()
        pendentes = Tarefa.objects.filter(concluida=False).count()

        taxa_conclusao = concluidas / total if total > 0 else 0

        dados = {
            "total": total,
            "concluidas": concluidas,
            "pendentes": pendentes,
            "taxa_conclusao": round(taxa_conclusao, 2)
        }

        return Response(dados, status=status.HTTP_200_OK)


class DetalheTarefaAPIView(APIView):

    def get_object(self, pk):
        return get_object_or_404(Tarefa, pk=pk)

    def get(self, request, pk, format=None):
        tarefa = self.get_object(pk)
        serializer = TarefaSerializer(tarefa)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        tarefa = self.get_object(pk)
        serializer = TarefaSerializer(tarefa, data=request.data)

        if serializer.is_valid():
            tarefa_atualizada = serializer.save()

            if tarefa_atualizada.concluida:
                tarefa_atualizada.data_conclusao = date.today()
                tarefa_atualizada.save()

            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        tarefa = self.get_object(pk)

        # REGRA DE NEGÓCIO (EXERCÍCIO 4)
        if (
            tarefa.prioridade == 'alta'
            and request.data.get('concluida') is True
        ):
            return Response(
                {
                    "erro": "Tarefas de alta prioridade só podem ser concluídas via PUT"
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = TarefaSerializer(
            tarefa,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()

            if request.data.get('concluida') is True:
                tarefa.data_conclusao = date.today()
                tarefa.save()

            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        tarefa = self.get_object(pk)
        tarefa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DuplicarTarefaAPIView(APIView):
    def post(self, request, pk, format=None):
        try:
            tarefa = get_object_or_404(Tarefa, pk=pk)
            tarefa.pk = None
            tarefa.titulo = f"{tarefa.titulo} (Cópia)"
            tarefa.concluida = False
            tarefa.data_conclusao = None
            tarefa.save()

            serializer = TarefaSerializer(tarefa)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except Exception as e:
            logger.error(f"Erro ao duplicar tarefa: {str(e)}")
            return Response(
                {'error': 'Erro interno do servidor.'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


# EXERCÍCIO 3 — PATCH EM LOTE
class ConcluirTodasTarefasAPIView(APIView):
    def patch(self, request, format=None):
        hoje = date.today()

        total_atualizadas = Tarefa.objects.filter(
            concluida=False
        ).update(
            concluida=True,
            data_conclusao=hoje
        )

        return Response(
            {
                "mensagem": "Todas as tarefas foram concluídas",
                "total_atualizadas": total_atualizadas
            },
            status=status.HTTP_200_OK
        )
