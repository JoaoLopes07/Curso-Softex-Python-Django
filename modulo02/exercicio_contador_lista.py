class Lista():
    def __init__(self, lista):
        self.lista = lista

    def procurar(self, numero):
        contador = 0
        for n in self.lista:
            if n == numero:
                contador += 1
        print(f'O número {numero} aparece {contador} vez(es)')
            
        

lista = [1, 5, 2, 5, 8, 5]

numero = int(input('Digite o número que você quer contar: '))

rodar = Lista(lista)
rodar.procurar(numero)