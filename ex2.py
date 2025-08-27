senha = input('Digite uma senha com pelo menos 8 caracteres: ')

caracteres = len(senha)

if caracteres <8:
    print('Digite pelo menos 8 caracteres')

else:
    print('Senha Válida')