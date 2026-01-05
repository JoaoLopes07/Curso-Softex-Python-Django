"""Somador de Números Positivos
● Use um while True para pedir números ao usuário.
● Some todos os números positivos.
● Se o usuário digitar um número negativo, use break para sair do loop e imprima a soma
total"""


class Numero:
    def soma(self):
        soma = 0
        while True:
            numero = int(
                input("Digite um número para somar ou número negativo para sair: ")
            )
            if numero > 0:
                soma += numero
            elif numero < 0:
                break
        print(f"A soma dos números positivos é {soma}")


rodar = Numero()
rodar.soma()
