''' Tabuada Simples 
● Peça um número ao usuário. 
● Use um while para imprimir a tabuada desse número, de 1 a 10.'''

class Numero():
    def __init__(self):
        numero = int(input('Digite o número para a tabuada: '))
        contador = 1
        while contador <=10:
            print(f'{numero} x {contador} = {numero * contador}')
            contador += 1
            continue

        
rodar = Numero()
 
