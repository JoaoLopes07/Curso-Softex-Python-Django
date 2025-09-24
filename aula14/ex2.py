class Midia:
    def __init__(self, titulo, duracao_seg):
        self.titulo = titulo
        self.duracao_seg = duracao_seg
    
    def exibir(self):
        print(f'Titúlo: {self.titulo}\nDuração: {self.duracao_seg} segundos')
    
class Musica(Midia):
    def __init__(self, titulo, duracao_seg, artista):
        super().__init__(titulo, duracao_seg)
        self.artista = artista
    def exibir(self):
        print(f'Título: {self.titulo}\nDuração: {self.duracao_seg} segundos\nArtista: {self.artista}')
    
class Video(Midia):
    def __init__(self, titulo, duracao_seg, resolucao):
        super().__init__(titulo, duracao_seg)
        self.resolucao = resolucao
    def exibir(self):
        print(f'Título: {self.titulo}\nDuração: {self.duracao_seg} segundos\nResolução: {self.resolucao}')

musica = Musica('Locked of Heaven', 300, 'Bruno Mars')
video = Video('Shape of you', 500, '4K')

dicionario = {'musica': [musica], 'video': [video]}

for l in dicionario.values():
    for i in l:
        i.exibir()