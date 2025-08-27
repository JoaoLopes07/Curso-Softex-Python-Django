palavra = input('Digite uma palavra: ')

print('A palavra tem', len(palavra), 'Caracteres')
if 'a' in palavra:
    print('(a) está na palavra digitada')
else:
    print('(a) não está na palavra digitada')