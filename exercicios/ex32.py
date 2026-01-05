"""Contador Regressivo
● Peça um número inteiro ao usuário.
● Use um while para fazer uma contagem regressiva a partir desse número até 0. Imprima
cada número."""


class Numero:
    def __init__(self):
        numero = int(input("Digite seu número inteiro: "))
        contador = numero
        while contador >= 0:
            print(contador)
            contador -= 1
            continue


rodar = Numero()
