'''Verificador de Par ou Ímpar
● Peça ao usuário um número inteiro.
● Use o operador de módulo (%) e uma estrutura if-else para determinar e imprimir se o
número é "par" ou "ímpar".
'''

class Numero():
    def __init__(self,numero):
        self.numero = numero
        
    def verificar(self):
        if self.numero % 2 == 0:
            print('O número é par')
        elif self.numero % 2 == 1:
            print('O número é impar')
    
numero = int(input('Digite um número inteiro: '))

rodar = Numero(numero)

rodar.verificar()