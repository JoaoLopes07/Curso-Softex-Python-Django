class Frase():
    def __init__(self, frase):
        self.frase = frase

frase = input('Digite uma frase: ').title()
print(frase)

rodar = Frase(frase)
