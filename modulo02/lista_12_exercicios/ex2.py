class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def apresentar(self):
        print(f"{self.nome} = R${self.preco:.2f}")


produto1 = Produto("Caderno", 15.50)
produto2 = Produto("Caneta", 3.00)

produto1.apresentar()
produto2.apresentar()
