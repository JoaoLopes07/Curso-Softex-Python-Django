usuario = input('Digite o seu Usúario: ')
senha = input('Digite sua senha: ')

if 'admin' in usuario and len(senha) >=6:
    print('Login Criado')
else:
    print('Usúario ou Senha inválido')