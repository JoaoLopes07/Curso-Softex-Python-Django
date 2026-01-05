"""Peça ao usuário para digitar um número inteiro.
● Use uma estrutura if simples para verificar se o número é maior que zero.
● Se for, imprima "O número é positivo!".
"""


class Numero:
    def __init__(self, numero):
        self.numero = numero

    def condicao(self):
        if self.numero > 0:
            print("Número Positivo")


numero = int(input("Digite um número inteiro: "))

rodar = Numero(numero)

rodar.condicao()
