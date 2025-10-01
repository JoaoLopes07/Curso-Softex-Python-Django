class Palavra():
    def __init__(self, palavra):
        self.palavra = palavra
        
    def verificar(self):
        if self.palavra.startswith("py"):
            print('A palavra começa com Py')
        else:
            print('A palavra não começa com Py')
    
palavra = input('Digite uma palavra: ').lower()

rodar = Palavra(palavra)

rodar.verificar()
