class Palavra:
    def __init__(self, texto):
        self.texto = texto

    def formatar(self):
        nova_palavra = (
            self.texto.replace("a", "1")
            .replace("e", "2")
            .replace("i", "3")
            .replace("o", "4")
            .replace("u", "5")
        )
        return nova_palavra


texto = input("Digite uma palavra: ")
codificador = Palavra(texto)
resultado = codificador.formatar()

print(resultado)
print(texto)
