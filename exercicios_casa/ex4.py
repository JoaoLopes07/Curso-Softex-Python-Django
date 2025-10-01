class Usuario():
    def __init__(self, usuario, senha):
        self.usuario = usuario
        self.senha = senha
        
    def verificar(self):
        if 'admin' in self.usuario and len(self.senha) >=6:
            print('Login Criado')
        else:
            print('Usúario ou Senha inválido')
    
usuario = input('Digite o seu Usúario: ')
senha = input('Digite sua senha: ')

rodar = Usuario(usuario, senha)

rodar.verificar()