palavra_proibida = 'spoiler'
while True:
    palavra = input('Digite a palavra até achar a proibida: ').lower()
    if palavra_proibida in palavra:
        print('Palavra proibida está na sua palavra')
        break



