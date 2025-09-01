class Senha():
    def verificar(self, senha):
        maiuscula = False
        minuscula = False
        numero = False
        simbolo = False
        cont = 0
        while cont < len(senha):
            caractere = senha[cont]
            if caractere.isupper():
                maiuscula = True
            elif caractere.islower():
                minuscula = True
            elif caractere.isdigit():
                numero = True
            elif not caractere.isalnum():
                simbolo = True
            cont += 1

        if len(senha) >=8 and maiuscula and minuscula and numero and simbolo:
            return True

        else:
            print('A Senha precisa ter:\n8 caracteres\n1 letra maiúscula\n1 letra minúscula\n1 número\n1 simbolo')
            return False

rodar = Senha()

while True:
    senha = input('Digite uma senha: ')
    if rodar.verificar(senha):
        print('Senha Válida')
        break

