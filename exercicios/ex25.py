'''Verificador de Divisibilidade
● Peça ao usuário um número inteiro.
● Verifique se o número é divisível por 5 (use o operador %).
● Se for, imprima "O número é divisível por 5".
'''

class Numero():
    def __init__(self, numero):
        self.numero = numero
        
    def verificar(self):
        if self.numero % 5 == 0:
            print('O número é divisível por 5')
        else:
            print('O número não é divisível por 5')
    
numero = int(input('Digite um número inteiro: '))

rodar = Numero(numero)

rodar.verificar()