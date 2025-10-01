class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade 
    
    def apresentar(self):
        print(f'Meu nome é {self.nome} e tenho {self.idade} anos')
    
class Estudante(Pessoa):
    def __init__(self, nome, idade, curso):
        super().__init__(nome, idade)
        self.curso = curso
    def apresentar(self):
        print(f'Meu nome é {self.nome} tenho {self.idade} anos e curso {self.curso}')

pessoa1 = Pessoa('Anderson', 18)

pessoa = Estudante('João', 21, 'Engenharia de Software')

lista = [pessoa1, pessoa]

for l in lista:
    l.apresentar()