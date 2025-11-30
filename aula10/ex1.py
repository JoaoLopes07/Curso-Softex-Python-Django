class Vendas():
    def __init__(self, vendas):
        self.vendas = vendas
    
    def compara(self):
        vendas_filtradas = []
        produtos_unicos = set()

        for produto, preco, quantidade in vendas:
            preco_final = preco * quantidade
            if preco_final >=100:
                vendas_filtradas.append((produto, preco, quantidade))
                produtos_unicos.add(produto)
        
        print(f'Vendas filtradas com valores iguais ou maior que 100:\n{vendas_filtradas}')
        print(f'\nProdutos únicos:\n{produtos_unicos}')


vendas = [('Teclado', 50, 2),
          ('Mouse', 25.50, 4),
          ('Monitor', 300, 1),
          ('Fone', 45, 1),
          ('Webcam', 75.20, 2)]

rodar = Vendas(vendas)

rodar.compara()

