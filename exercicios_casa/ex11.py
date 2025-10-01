class Frase():
    def __init__(self, frase, palavra1, palavra2):
        self.frase = frase
        self.palavra1 = palavra1
        self.palavra2 = palavra2
        
    def substituir(self):
        nova_frase = self.frase.replace(self.palavra1, self.palavra2)
        print(nova_frase)

frase = input('Digite uma frase: ')
palavra1 = input('Digite uma palavra pra substituir: ')
palavra2 = input('Qual palavra quer colocar no lugar? ')

rodar = Frase(frase, palavra1, palavra2)

rodar.substituir()