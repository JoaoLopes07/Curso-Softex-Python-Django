''' Acumulador de Soma
● Peça ao usuário para digitar 5 números.
● Use um while com um contador para somar todos os números digitados e imprimir o
resultado final.
'''

class Numero():
    def soma(self):
        contador = 0
        soma = 0
        while contador <5:
            numero = int(input('Digite um número: '))
            contador += 1
            soma += numero
        print(f'A soma dos 5 números é {soma}')

rodar = Numero()

rodar.soma()