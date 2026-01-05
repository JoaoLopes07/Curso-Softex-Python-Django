"""Dispositivos de um Computador (Fácil/Médio)
● Classes: Teclado, Mouse, Monitor e Computador.
● Classes Teclado, Mouse, Monitor:
○ Método: __init__ (sem atributos).
○ Método: ligar() que imprime uma mensagem indicando que o dispositivo está ligado
(ex: "O teclado foi ativado.").
● Classe Computador:
○ Atributos (Composição): teclado, mouse e monitor, que devem ser instâncias das
classes correspondentes.
○ Método: __init__ que inicializa os três atributos.
○ Método: ligar_computador() que chama o método ligar() de cada um dos seus
dispositivos."""


class Teclado:
    def ligar(self):
        print("O Teclado foi ativado")


class Mouse:
    def ligar(self):
        print("O Mouse foi ativado")


class Monitor:
    def ligar(self):
        print("O Monitor foi ativado")


class Computador:
    def __init__(self):
        self.teclado = Teclado()
        self.Mouse = Mouse()
        self.Monitor = Monitor()

    def ligar_computador(self):
        self.teclado.ligar()
        self.Mouse.ligar()
        self.Monitor.ligar()


rodar = Computador()
rodar.ligar_computador()
