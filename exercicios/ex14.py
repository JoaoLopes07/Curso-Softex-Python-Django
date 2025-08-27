senha = input('Digite uma senha com letra e números: ')

if senha.isalnum():
    print('Senha Válida')
else:
    print('Senha Inválida')