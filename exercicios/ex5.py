class Palavra():
    def __init__(self, palavra):
        self.palavra = palavra

    def verificar(self):
        if 'a' in self.palavra:
            print('(a) está na palavra digitada')
        else:
            print('(a) não está na palavra digitada')
    
palavra = input('Digite uma palavra: ')
print('A palavra tem', len(palavra), 'Caracteres')

rodar = Palavra(palavra)

rodar.verificar()