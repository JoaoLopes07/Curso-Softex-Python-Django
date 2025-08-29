'''Desafio de Programação: Validação de Triângulo
Seu objetivo: Escrever um algoritmo em Python que determine se três valores, fornecidos pelo usuário, podem formar um triângulo.'''

class Triangulo:
    def __init__(self, a, b, c):
        if a.isdigit() and b.isdigit() and c.isdigit():
            self.a, self.b, self.c = int(a), int(b), int(c)
            self.valido = True
        else:
            print('Apenas números inteiros positivos são aceitos')
            self.a = self.b = self.c = 0
            self.valido = False
        
    def validar(self):
        if not self.valido:
            return False
        if (self.a > 0 and self.b > 0 and self.c > 0 and self.a < self.b + self.c and
                self.b < self.a + self.c and
                self.c < self.a + self.b and
                self.a > abs(self.b - self.c) and
                self.b > abs(self.a - self.c) and
                self.c > abs(self.a - self.b)):
            return True
        else:
            return False
        
a = input('Digite o Lado A: ')
b = input('Digite o Lado B: ')
c = input('Digite o Lado C: ')
    
triangulo = Triangulo(a, b, c)

if triangulo.valido:  
    if triangulo.validar():
        print('Podem formar um Triângulo')
    else:
        print('Não podem formar um Triângulo')
    
        
    
        