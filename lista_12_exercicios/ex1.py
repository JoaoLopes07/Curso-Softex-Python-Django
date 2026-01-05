class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos")


pessoa1 = Pessoa("João", 25)
pessoa2 = Pessoa("Maria", 30)

pessoa1.apresentar()
pessoa2.apresentar()
