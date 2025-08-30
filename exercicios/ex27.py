'''Exercício 5: Maior de Dois Números
● Peça ao usuário para digitar dois números inteiros.
● Use if-else para descobrir qual dos dois é o maior e imprima o resultado.
'''

class Numero():
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2
        
    def verificar(self):
        if self.numero1 > self.numero2:
            print(f'O maior número é o {self.numero1}')
        elif self.numero2 > self.numero1:
            print(f'O maior número é o {self.numero2}')
        else:
            print(f'Os números são iguais')
    
numero1 = int(input('Digite um número inteiro: '))
numero2 = int(input('Digite outro número inteiro: '))

rodar = Numero(numero1, numero2)

rodar.verificar()