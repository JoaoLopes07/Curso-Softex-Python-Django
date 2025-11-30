class Cachorro:
    def __init__(self,nome, cor):
        self.nome = nome
        self.cor = cor

    def latir(self):
        print(f'{self.nome} diz: Au, Au!')

rodar = Cachorro('Pitbull', 'marrom')

rodar.latir()   