class Telefone:
    def __init__(self, numero):
        self.numero = numero

    def valido(self):
        return self.numero.isdigit() and len(self.numero) == 11

    def repeticao(self):
        for i in range(len(self.numero)):
            repeticoes = 0
            for j in range(len(self.numero)):
                if self.numero[i] == self.numero[j]:
                    repeticoes += 1
            if repeticoes >= 3:
                return True
        return False

    def formatar(self):
        ddd = self.numero[:2]
        parte1 = self.numero[2:7]
        parte2 = self.numero[7:12]
        return f"({ddd}) {parte1}-{parte2}"


numero = input("Digite seu telefone: ")
telefone = Telefone(numero)

if telefone.valido():
    if telefone.repeticao():
        print("Número Inválido por conter 3+ dígitos iguais")
    else:
        print(telefone.formatar())
else:
    print("Número inválido. Digite 11 dígitos")
