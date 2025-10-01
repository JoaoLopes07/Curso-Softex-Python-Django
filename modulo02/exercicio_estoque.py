class Estoque():
    def __init__(self, estoque_principal, estoque_online):
        self.estoque_principal = estoque_principal
        self.estoque_online = estoque_online

    def compara(self):
        produtos_ambos = set()
        produtos_loja = set()
        produtos_site = set()
        for produto, valor in self.estoque_principal:
            for produto2, valor2 in self.estoque_online:
                if produto == produto2:
                    produtos_ambos.add((produto, valor))

        for produto, valor in self.estoque_principal:
            if (produto, valor) not in self.estoque_online:
                produtos_loja.add((produto, valor))

        for produto2, valor2 in self.estoque_online:
            if (produto2, valor2) not in self.estoque_principal:
                produtos_site.add((produto2, valor2))
        
        print(f'Produtos em ambos os estoques: {produtos_ambos}\nProdutos apenas na loja: {produtos_loja}\nProdutos apenas no site: {produtos_site}')
        

estoque_principal = [('Camiseta', 101), ('Calça', 102), ('Boné', 103), ('Tênis', 104)]
estoque_online = [('Boné', 103), ('Camisa Polo', 105), ('Calça', 102), ('Chinelo', 106)]

rodar = Estoque(estoque_principal, estoque_online)

rodar.compara()
