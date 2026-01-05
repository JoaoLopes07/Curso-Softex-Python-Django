"""Avaliador de Notas
● Peça a nota de um aluno (float).
● Use if-elif-else para atribuir um conceito:
○ = 9.0: Conceito A
○ = 7.0: Conceito B
○ = 5.0: Conceito C
○ < 5.0: Conceito D"""


class Nota:
    def __init__(self, nota):
        self.nota = nota

    def Verificar(self):
        if self.nota >= 9 and self.nota <= 10:
            print("A")
        elif self.nota >= 7 and self.nota < 9:
            print("B")
        elif self.nota >= 5 and self.nota < 7:
            print("C")
        elif self.nota < 0 or self.nota > 10:
            print("Nota Inválida")
        else:
            print("D")


nota = float(input("Digite sua nota: "))

rodar = Nota(nota)

rodar.Verificar()
