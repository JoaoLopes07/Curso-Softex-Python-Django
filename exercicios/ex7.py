class Nome():
    def __init__(self, nome1, nome2):
        self.nome1 = nome1
        self.nome2 = nome2
    
    def verificar(self):
        if self.nome1 == self.nome2:
            print('Os Nomes são iguais')
        else:
            print('Os Nomes são diferentes')
    
nome1 = input('Digite o 1° nome: ').lower()
nome2 = input('Digite o 2° nome: ').lower()

rodar = Nome(nome1, nome2)

rodar.verificar()