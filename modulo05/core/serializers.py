from rest_framework import serializers
from .models import Tarefa
from datetime import date

class TarefaSerializer(serializers.ModelSerializer):

    titulo = serializers.CharField(
        max_length=200,
        error_messages={
            'required': 'O título é obrigatório.',
            'blank': 'O título não pode ser vazio.',
            'max_length': 'O título não pode ter mais de 200 caracteres.'
        }
    )

    data_conclusao = serializers.DateField(
        required=False,
        allow_null=True
    )

    class Meta:
        model = Tarefa
        fields = ['id', 'titulo', 'concluida', 'criada_em', 'prioridade', 'prazo', 'data_conclusao']
        read_only_fields = ['id', 'criada_em']

    def validate_titulo(self, value):
        value = value.strip()

        if not value:
            raise serializers.ValidationError(
                "O título não pode ser vazio ou conter apenas espaços."
            )

        if len(value) < 3:
            raise serializers.ValidationError(
                "O título deve ter pelo menos 3 caracteres."
            )

        if value.isdigit():
            raise serializers.ValidationError(
                "O título não pode conter apenas números."
            )

        return value

    def validate_data_conclusao(self, value):
        if value and value < date.today():
            raise serializers.ValidationError(
                "A data de conclusão não pode ser uma data no passado."
            )
        return value

    def validate(self, data):
        prazo = data.get('prazo')
        concluida = data.get('concluida')
        data_conclusao = data.get('data_conclusao')

        # Validação prazo
        if prazo and prazo < date.today():
            raise serializers.ValidationError(
                {'prazo': 'O prazo não pode ser uma data no passado.'}
            )

        if not concluida and prazo is None:
            raise serializers.ValidationError(
                {'prazo': 'O prazo é obrigatório quando a tarefa não está concluída.'}
            )

        # Validação data_conclusao + concluida
        if concluida and not data_conclusao:
            raise serializers.ValidationError(
                {'data_conclusao': 'A data de conclusão é obrigatória quando a tarefa está concluída.'}
            )

        if not concluida and data_conclusao:
            raise serializers.ValidationError(
                {'data_conclusao': 'A data de conclusão só pode ser preenchida quando a tarefa estiver concluída.'}
            )

        return data
