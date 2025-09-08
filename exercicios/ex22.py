'''Peça ao usuário para digitar o preço original de um produto (float).
● Se o preço for maior que R$ 100,00, aplique um desconto de 10% e imprima o novo
preço.
● Use o operador de multiplicação (*) e subtração (-).
'''

class Preco():
    def __init__(self, preco):
        self.preco = preco

    def desconto(self):
        if preco > 100:
            desconto = preco - (preco * 0.10)
            print(f'O preço com desconto ficou R${desconto}')
        else:
            print('Preço sem desconto')

preco = float(input('Digite o preço do produto: '))

rodar = Preco(preco)

rodar.desconto()

