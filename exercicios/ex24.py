'''Exercício 2: Calculadora de Desconto
● Peça ao usuário para digitar o preço original de um produto (float).
● Se o preço for maior que R$ 100,00, aplique um desconto de 10% e imprima o novo
preço.
● Use o operador de multiplicação (*) e subtração (-).'''

class Preco:
    def __init__(self,preco, desconto):
        self.preco = preco
        self.desconto = desconto
    
    def verificar(self):
        if self.preco > 100:
            desconto_total = self.preco * self.desconto
            preco_final = self.preco - desconto_total
            print(f'Seu novo preço com o desconto é de R${preco_final:.2f}')
            
        else:
            print('Preço sem desconto')
            
        
preco = float(input('Digite o preço do produto: '))
desconto = 0.10

rodar = Preco(preco, desconto)

rodar.verificar()


