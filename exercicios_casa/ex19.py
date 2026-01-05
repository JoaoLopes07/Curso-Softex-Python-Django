class Numero:
    def __init__(self, numero):
        self.numero = numero

    def maior(self):
        for i in range(4):
            maior = int(input("Digite outro número inteiro: "))

        if maior > self.numero:
            self.numero = maior
        print(f"O maior número digitado foi o {self.numero}")


numero = int(input("Digite um número inteiro: "))

rodar = Numero(numero)
rodar.maior()
