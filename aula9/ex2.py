class Lista():
    def __init__(self, lista1, lista2):
        self.lista1 = lista1
        self.lista2 = lista2

    def encontrar(self):
        lista3 = []
        for n in self.lista1:
            for m in self.lista2:
                if n == m:
                    lista3.append(n)
        print(lista3)

lista1 = ['vermelho', 'azul', 'verde', 'amarelo']
lista2 = ['verde', 'roxo', 'azul', 'preto']

rodar = Lista(lista1, lista2)

rodar.encontrar()