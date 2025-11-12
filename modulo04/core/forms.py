from django import forms
from .models import Tarefa # Importe o Model
# Esta classe herda de 'ModelForm'
class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = ['titulo']