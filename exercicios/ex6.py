class Palavra():

    def verificar(self):
        while True:
            self.palavra = input('Digite uma palavra: ').lower()
            if len(self.palavra) <3:
                print('A palavra precisa ter no minímo 3 caracteres')
            elif not self.palavra[0] == 'p':
                print('A palavra deve começar com a letra P')
            elif self.palavra[len(self.palavra) - 1] != 's':
                print('A palavra deve terminar com S')
            elif 'i' not in self.palavra:
                print('A palavra deve conter a letra I')
            elif 'm' in self.palavra or 'n' in self.palavra:
                print('A palavra não pode contar as letras M e N')
            else:
                print('Palavra Aceita')
                break
            
rodar = Palavra()

rodar.verificar()
