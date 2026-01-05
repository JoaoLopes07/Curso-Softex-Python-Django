from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User, Group
from django.urls import reverse
from core.models import Tarefa


class TarefaAPITest(APITestCase):
    """
    Testes de Integração para os endpoints de Tarefa.
    Simula o ciclo completo: Request -> URL -> View -> Serializer -> DB -> Response
    """

    def setUp(self):
        """Prepara a massa de dados para os testes."""
        # 1. Criar usuários
        self.user1 = User.objects.create_user(username='usuario1', password='senha123')
        self.user2 = User.objects.create_user(username='usuario2', password='senha456')

        # 2. Criar e atribuir grupos (se sua lógica depender disso)
        self.grupo_comum = Group.objects.create(name='Comum')
        self.user1.groups.add(self.grupo_comum)

        # 3. Criar tarefas iniciais
        self.tarefa_user1 = Tarefa.objects.create(
            user=self.user1,
            titulo='Tarefa do User 1',
            concluida=False
        )
        self.tarefa_user2 = Tarefa.objects.create(
            user=self.user2,
            titulo='Tarefa do User 2',
            concluida=True
        )

    # ------------------ Helpers ------------------
    def obter_token(self, username, password):
        """
        Método auxiliar para realizar login e obter o token JWT.
        Evita repetição de código nos testes.
        """
        url = reverse('token_obter_pair')  # Nome da rota definida no urls.py
        response = self.client.post(url, {
            'username': username,
            'password': password
        }, format='json')
        return response.data['access']
