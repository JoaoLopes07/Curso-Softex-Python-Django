class Palavra():
    def __init__(self, palavra):
        self.palavra = palavra
    
    def numerico(self):
        print(self.palavra.isdigit())

palavra = input('Digite qualquer coisa: ')

rodar = Palavra(palavra)

rodar.numerico()

