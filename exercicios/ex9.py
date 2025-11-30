class Texto():
    def __init__(self, texto):
        self.texto = texto

texto = input('Digite um texto com espaços iniciais e finais: ').strip()
print(texto)

rodar = Texto(texto)
