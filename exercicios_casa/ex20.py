class Numero:
    def __init__(self, numero):
        self.numero = numero

    def condicao(self):
        for i in range(1, numero + 1):
            print("*" * 1)


numero = int(input("Digite um numero inteiro: "))

rodar = Numero(numero)

rodar.condicao()
