class Lista:
    def __init__(self, lista):
        self.lista = lista

    def nota(self):
        notas = 0
        maior = []
        menor = []
        for _, nota in self.lista:
            if nota > notas:
                notas = nota
        print(f"A maior nota é: {notas}")

        for aluno, nota in self.lista:
            if nota == notas:
                maior.append(aluno)
                aluno_maior = tuple(maior)
        print(f"Alunos que tiraram a maior nota: {aluno_maior}")

        for aluno, nota in self.lista:
            if nota < 7:
                menor.append(aluno)
                aluno_menor = set(menor)
        print(f"Alunos que tiveram nota abaixo de 7: {aluno_menor}")


lista = [
    ("Ana", 9.5),
    ("João", 8.0),
    ("Maria", 10.0),
    ("Pedro", 7.5),
    ("Ana", 10.0),
    ("Carlos", 6.5),
]

rodar = Lista(lista)

rodar.nota()
