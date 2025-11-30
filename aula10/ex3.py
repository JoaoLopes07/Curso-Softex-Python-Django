class Acessos():
    def __init__(self, acessos):
        self.acessos = acessos

    def compara(self):
        set_sucessos = set()
        set_falhas = set()

        for nome, status in self.acessos:
            if status == 'sucesso':
                set_sucessos.add(nome)
            if status == 'falha' and nome not in set_sucessos:
                set_falhas.add(nome)

        print(set_sucessos)
        print(set_falhas)


acessos = [('Pedro', 'sucesso'), ('Ana', 'falha'), ('Maria', 'sucesso'), ('Pedro', 'falha'), ('Ana', 'falha')]

rodar = Acessos(acessos)

rodar.compara()