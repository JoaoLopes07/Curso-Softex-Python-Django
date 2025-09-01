class Lista():
    def __init__(self, numero):
        self.numero = numero
        self.primos = []

    def nova_lista(self):
        for n in self.numero:
            primo = True
            if n <2:
                primo = False
            else:
                for i in range(2, n):
                    if n % i == 0:
                        primo = False
                        break
                if primo:
                    self.primos.append(n)
        print(f'Os números primos são {self.primos}')

        

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

rodar = Lista(lista)

rodar.nova_lista()
