class Palavra():
    def __init__(self, palavra):
        self.palavra = palavra
    
    def contador(self):
        contador_vogais = 0
        for letra in palavra:
            if 'a' == letra or 'e' == letra or 'i' == letra or 'o' == letra or 'u' == letra:
                contador_vogais += 1
        print(contador_vogais)

palavra = input('Digite uma palavra: ').lower()

rodar = Palavra(palavra)
rodar.contador()

