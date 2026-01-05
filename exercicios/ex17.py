class Tabuada:
    def __init__(self):
        self.tabuada = tabuada

    def conta(self):
        for numero in range(1, 11):
            print(f"{tabuada} x {numero} = {tabuada*numero}")


tabuada = int(input("Digite um número inteiro: "))

rodar = Tabuada()

rodar.conta()
