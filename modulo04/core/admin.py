from django.contrib import admin
from .models import Tarefa # 1. Importe seu Model
from .models import Alunos
# 2. "Registre" seu Model no sit
admin.site.register(Tarefa)
admin.site.register(Alunos)
