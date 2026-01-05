"""Categoria de CNH
● Peça a idade e se o usuário tem CNH (True ou False).
● Use if-elif-else com operadores lógicos (and e or) para:
○ Se for maior de 18 e tiver CNH: "Pode dirigir."
○ Se for maior de 18 e não tiver CNH: "Precisa tirar a CNH."
○ Se for menor de 18: "Não pode dirigir."""


class Idade:
    def __init__(self, idade, cnh):
        self.idade = idade
        self.cnh = None

    def verificar(self):
        if self.idade >= 18 and self.cnh == "sim":
            print("Pode dirigir")

        elif self.idade >= 18 and self.cnh == "nao":
            print("Precisa tirar a cnh")

        elif self.cnh != "nao" or self.cnh != "sim":
            return cnh

        else:
            print("Não pode dirigir")


idade = int(input("Digite a sua idade: "))
cnh = input("Você tem CNH? Responda com sim ou nao: ")

usuario = Idade(idade, cnh)
usuario.verificar()
