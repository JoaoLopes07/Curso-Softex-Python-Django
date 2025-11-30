''': Login com Tentativas
● Defina uma senha secreta.
● Use um while True e um contador de tentativas (máximo de 3).
● Se o usuário acertar a senha, imprima "Login bem-sucedido!" e use break.
● Se o usuário errar 3 vezes, imprima "Tentativas esgotadas!" e pare o programa'''

class Login():
    def senha(self):
        senha_secreta = 'python'
        cont = 0
        while cont <3:
            senha = input('Qual a senha? ')
            if senha == senha_secreta:
                print('Login bem-sucedido')
                break
            elif senha != senha_secreta:
                print('Senha errada')
                cont +=1
        if cont >=3:
            print('Tentativas esgotadas')
            

rodar = Login()
rodar.senha()