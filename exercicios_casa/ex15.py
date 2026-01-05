class Palavra:
    def __init__(self, palavra):
        self.palavra = palavra

    def verificar(self):
        while True:
            self.palavra = input("Digite a palavra até achar a proibida: ").lower()
            if palavra in self.palavra:
                print("Palavra proibida está na sua palavra")
                break


palavra = "spoiler"
rodar = Palavra(palavra)
rodar.verificar()
