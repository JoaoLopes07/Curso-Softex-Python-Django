class Palavra():
    def __init__(self, palavra, letra):
        self.palavra = palavra
        self.letra = letra
        
    def verificar(self):
        if self.letra in self.palavra:
            print('A letra está na palavra')
        else:
            print('A letra não está na palavra')
    
palavra = input('Digite uma palavra: ').lower()
letra = input('Digite uma letra: ').lower()

rodar = Palavra(palavra, letra)

rodar.verificar()