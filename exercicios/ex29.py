'''Classificador de Idade
● Peça a idade de uma pessoa.
● Use if-elif-else para classificar a idade em:
○ "Criança" (0 a 12 anos)
○ "Adolescente" (13 a 17 anos)
○ "Adulto" (18 a 59 anos)
○ "Idoso" (60 anos ou mais)'''

class Idade():
    def __init__(self, idade):
        self.idade = idade
        
    def verificar(self):
        if self.idade > 0 and self.idade <= 12:
            print('Você é uma Criança')
        elif self.idade >= 13 and self.idade <= 17:
            print('Você é um Adolescente')
        elif self.idade >=18 and self.idade <=59:
            print('Você é um Adulto')
        else:
            print('Você é um Idoso')
    
idade = int(input('Digite a sua idade: '))

rodar = Idade(idade)

rodar.verificar()