'''Exercício 1: Verificador de Positivo
● Peça ao usuário para digitar um número inteiro.
● Use uma estrutura if simples para verificar se o número é maior que zero.
● Se for, imprima "O número é positivo!".'''

class Numero:
    def __init__(self, numero):
        self.numero = numero
    
    def verificacao(self):      
            if self.numero > 0:
                print('O número é positivo')
            else:
                print('Número Inválido!')

numero = int(input('Digite seu número: '))

numero = Numero(numero)

numero.verificacao()