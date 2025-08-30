class Texto():
    def __init__(self, texto, letra):
        self.texto = texto
        self.letra = letra
    
    def count(self):
        contador = self.texto.count(self.letra)
        print(contador)
        


texto = input('Digite um texto: ')
letra = input('Digite uma letra: ')

rodar = Texto(texto, letra)

rodar.count()
