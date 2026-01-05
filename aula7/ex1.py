class Robo:
    def andar(self):
        robo = 0

        while True:
            print(
                "\n"
                "===Menu de Opções===\n\nDigite 1 para Avançar\nDigite 2 para Recuar\nDigite 3 para Status\nDigite 4 para Desligar\n"
            )

            numero = int(input("Digite seu comando: "))

            if numero == 1:
                robo += 1
            elif numero == 2:
                robo -= 1
            elif numero == 3:
                print(f"\nO robo está na posição {robo}")
            elif numero == 4:
                print("Desligando robo...")
                break
            else:
                print("\nOpção Inválida")


rodar = Robo()

rodar.andar()
