class Lista:
    def __init__(self):
        self.lista = []

    def verificar(self, numero):
        if numero == "-1":
            return False

        if numero.isdigit():
            n = int(numero)
            if n >= 0 and n <= 100:
                self.lista.append(n)
            else:
                print("Digite apenas números entre 0 e 100")
        else:
            ("Digite apenas números")

        return True


rodar = Lista()

while True:
    numero = input("Digite um número entre 0 e 100 ou -1 para parar: ")
    if not rodar.verificar(numero):
        break
print("Lista final:", rodar.lista)
