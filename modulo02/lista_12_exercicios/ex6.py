class Funcionario:
    percentual_bonus = 1.10

    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def aplicar_bonus(self):
        self.salario *= Funcionario.percentual_bonus
        print(f"{self.nome} recebeu bônus. Novo salário: R$ {self.salario:.2f}")


f1 = Funcionario("João", 2000)
f2 = Funcionario("Maria", 3500)

f1.aplicar_bonus()
f2.aplicar_bonus()
