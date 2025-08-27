

while True:
    palavra = input('Digite uma palavra: ').lower()
    if len(palavra) <3:
        print('A palavra precisa ter no minímo 3 caracteres')
    elif not palavra[0] == 'p':
        print('A palavra deve começar com a letra P')
    elif palavra[len(palavra) - 1] != 's':
        print('A palavra deve terminar com S')
    elif 'i' not in palavra:
        print('A palavra deve conter a letra I')
    elif 'm' in palavra or 'n' in palavra:
        print('A palavra não pode contar as letras M e N')
    else:
        print('Palavra Aceita')
        break
