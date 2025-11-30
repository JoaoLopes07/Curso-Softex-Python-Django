class Frase():
    def __init__(self, frase):
        self.frase = frase
        
    def verificar(self):
        if 'bomba' in self.frase:
            print('A palavra bomba aparece na frase')
        else:
            print('A palavra bomba não aparece na frase')
            
frase = input('Digite uma frase: ')

rodar = Frase(frase)

rodar.verificar()