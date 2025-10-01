class Senha():
    def __init__(self, senha):
        self.senha = senha
        
    def verificar(self):
        caracteres = len(senha)
        if caracteres <8:
            print('Digite pelo menos 8 caracteres')
        else:
            print('Senha Válida')

senha = input('Digite uma senha com pelo menos 8 caracteres: ')

rodar = Senha(senha)

rodar.verificar()