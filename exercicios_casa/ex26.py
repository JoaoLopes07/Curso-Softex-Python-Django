"""Verificador de Senha
● Defina uma senha secreta em uma variável (str, por exemplo, "python123").
● Peça ao usuário para digitar uma senha.
● Use if-else para verificar se a senha digitada é igual à senha secreta. Imprima "Acesso
concedido" ou "Senha incorreta".
"""


class Senha:
    def verificar(self):
        while True:
            senha = input("Digite uma senha: ")
            if senha == senha_secreta:
                print("Acesso concedido!")
                break
            else:
                print("Acesso Negado!")


senha_secreta = str("python")

rodar = Senha()

rodar.verificar()
