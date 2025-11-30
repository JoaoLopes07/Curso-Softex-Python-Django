class Senha():
    def __init__(self, senha):
        self.senha = senha

    def verificar(self):
        if self.senha.isalnum():
            print('Senha Válida')
        else:
            print('Senha Inválida')

senha = input('Digite uma senha com letra e números: ')

rodar =Senha(senha)

rodar.verificar()